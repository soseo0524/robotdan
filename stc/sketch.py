import pygame
import sys
import math
import random

# 단위 -> 픽셀 스케일
SCALE = 6
MARGIN = 60

# 전체 맵 크기 (W, H)
W, H = 100, 100

# 사각형 1: 좌상단 꼭짓점(0,0) 기준 (+x 23, -y 24), 크기 (13,17)
r1_x, r1_y = 23, -24
r1_w, r1_h = 13, 17

# 사각형 2: 우하단 꼭짓점(W,-H) 기준 (-x 33, +y 50), 크기 (7,10)
rb_x, rb_y = W, -H
r2_x = rb_x - 26
r2_y = rb_y + 40
r2_w, r2_h = 7, 10

pygame.init()
screen_w = W * SCALE + 2 * MARGIN
screen_h = H * SCALE + 2 * MARGIN
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Mapex - Autonomous Coverage Path Planning")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 14)

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
FILL = (160, 160, 160)
CAR_COLOR = (255, 100, 100)  # 빨간색 자동차
WAYPOINT_COLOR = (0, 255, 0)  # 초록색 waypoint
CURRENT_WAYPOINT_COLOR = (0, 200, 0)  # 현재 목표 waypoint

origin_x = MARGIN
origin_y = MARGIN

def world_to_screen(x, y):
    sx = origin_x + int(x * SCALE)
    sy = origin_y + int((-y) * SCALE)
    return sx, sy

def world_rect_to_screen(x, y, w, h):
    tlx, tly = world_to_screen(x, y)
    rect = pygame.Rect(tlx, tly, int(w * SCALE), int(h * SCALE))
    return rect

# 맵 외곽
map_rect = pygame.Rect(origin_x, origin_y, W * SCALE, H * SCALE)

# 장애물 사각형
rect1 = world_rect_to_screen(r1_x, r1_y, r1_w, r1_h)
rect2 = world_rect_to_screen(r2_x, r2_y, r2_w, r2_h)

# 자동차: 가로 11, 세로 20
car_w, car_h = 11, 20
car_x, car_y = 10, -10  # 월드 좌표
car_speed_world = 0.5  # 이동 속도

# Waypoint 생성 (STC - Steiner Tree Coverage 알고리즘)
def is_cell_occupied(grid_x, grid_y, cell_size):
    """셀이 장애물과 겹치는지 확인"""
    cell_rect = pygame.Rect(
        origin_x + grid_x * cell_size * SCALE,
        origin_y + grid_y * cell_size * SCALE,
        cell_size * SCALE,
        cell_size * SCALE
    )
    return cell_rect.colliderect(rect1) or cell_rect.colliderect(rect2)

def generate_waypoints_stc():
    """
    STC 알고리즘으로 최적 waypoint 생성
    1. 맵을 그리드로 분할
    2. 장애물을 고려한 그래프 생성
    3. 모든 셀을 커버하는 최소 비용 경로 탐색
    4. 최적의 waypoint 생성
    """
    cell_size = 15  # 그리드 셀 크기
    grid_w = W // cell_size + 1
    grid_h = H // cell_size + 1
    
    # Step 1: 맵을 그리드로 분할 - 무장애 셀 찾기
    free_cells = []
    for gy in range(grid_h):
        for gx in range(grid_w):
            if not is_cell_occupied(gx, gy, cell_size):
                free_cells.append((gx, gy))
    
    # Step 2: 그래프 생성 (인접한 무장애 셀)
    def get_neighbors(cell):
        x, y = cell
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in free_cells:
                neighbors.append((nx, ny))
        return neighbors
    
    # Step 3: DFS로 모든 셀을 방문하는 경로 찾기 (Eulerian path 근사)
    visited = set()
    path = []
    
    def dfs(cell):
        if cell in visited:
            return
        visited.add(cell)
        path.append(cell)
        for neighbor in get_neighbors(cell):
            if neighbor not in visited:
                dfs(neighbor)
    
    if free_cells:
        start_cell = min(free_cells)  # 좌상단부터 시작
        dfs(start_cell)
    
    # Step 4: 그리드 좌표를 월드 좌표로 변환하여 waypoint 생성
    waypoints = []
    for gx, gy in path:
        wp_x = gx * cell_size + cell_size // 2
        wp_y = -(gy * cell_size + cell_size // 2)
        # 월드 좌표 범위 내에 있는지 확인
        if 0 <= wp_x <= W and -H <= wp_y <= 0:
            waypoints.append((wp_x, wp_y))
    
    return waypoints if waypoints else [(50, -50)]

waypoints = generate_waypoints_stc()
current_waypoint_idx = 0

# 경로 추적용 Surface
trail_surface = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
trail_surface.fill((0, 0, 0, 0))

car_rect = world_rect_to_screen(car_x, car_y, car_w, car_h)

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_direction_to_waypoint(car_x, car_y, wp_x, wp_y):
    dx = wp_x - car_x
    dy = wp_y - car_y
    return math.atan2(dy, dx)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 현재 목표 waypoint
    if current_waypoint_idx < len(waypoints):
        target_x, target_y = waypoints[current_waypoint_idx]
        
        # 거리 계산
        distance = get_distance(car_x, car_y, target_x, target_y)
        
        # Waypoint 근처면 다음 waypoint로 이동
        if distance < 2:
            current_waypoint_idx += 1
        else:
            # 목표 waypoint로 향하는 방향 계산
            target_direction = get_direction_to_waypoint(car_x, car_y, target_x, target_y)
            
            # 다음 위치 계산
            next_x = car_x + car_speed_world * math.cos(target_direction)
            next_y = car_y + car_speed_world * math.sin(target_direction)
            next_rect = world_rect_to_screen(next_x, next_y, car_w, car_h)
            
            # 경계 및 장애물 체크
            can_move = True
            if (next_x < 0 or next_x + car_w > W or 
                next_y - car_h < -H or next_y > 0):
                can_move = False
                # 경계에 닿으면 다음 waypoint로 스킵
                current_waypoint_idx += 1
            elif next_rect.colliderect(rect1) or next_rect.colliderect(rect2):
                can_move = False
                # 장애물에 닿으면 다음 waypoint로 스킵
                current_waypoint_idx += 1
            
            if can_move:
                car_x = next_x
                car_y = next_y
    else:
        # 모든 waypoint 완료 - 처음부터 다시
        current_waypoint_idx = 0
    
    car_rect = world_rect_to_screen(car_x, car_y, car_w, car_h)
    
    # 경로 그리기
    pygame.draw.rect(trail_surface, (255, 100, 100, 150), car_rect)

    # 화면 그리기
    screen.fill(WHITE)
    
    # 맵 경계
    pygame.draw.rect(screen, BLACK, map_rect, 2)
    
    # 경로 표시
    screen.blit(trail_surface, (0, 0))
    
    # 장애물
    pygame.draw.rect(screen, FILL, rect1)
    pygame.draw.rect(screen, BLACK, rect1, 2)
    pygame.draw.rect(screen, FILL, rect2)
    pygame.draw.rect(screen, BLACK, rect2, 2)
    
    # Waypoint 표시
    for i, (wp_x, wp_y) in enumerate(waypoints):
        wp_screen = world_to_screen(wp_x, wp_y)
        color = CURRENT_WAYPOINT_COLOR if i == current_waypoint_idx else WAYPOINT_COLOR
        pygame.draw.circle(screen, color, wp_screen, 4)
    
    # 자동차
    pygame.draw.rect(screen, CAR_COLOR, car_rect)
    pygame.draw.rect(screen, BLACK, car_rect, 2)
    
    # 정보 표시
    info_text = f"Waypoint: {current_waypoint_idx}/{len(waypoints)}"
    info_surf = FONT.render(info_text, True, BLACK)
    screen.blit(info_surf, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)
