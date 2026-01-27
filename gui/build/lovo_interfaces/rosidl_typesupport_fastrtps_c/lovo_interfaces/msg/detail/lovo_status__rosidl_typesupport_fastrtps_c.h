// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice
#ifndef LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "lovo_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "lovo_interfaces/msg/detail/lovo_status__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
bool cdr_serialize_lovo_interfaces__msg__LovoStatus(
  const lovo_interfaces__msg__LovoStatus * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
bool cdr_deserialize_lovo_interfaces__msg__LovoStatus(
  eprosima::fastcdr::Cdr &,
  lovo_interfaces__msg__LovoStatus * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
size_t get_serialized_size_lovo_interfaces__msg__LovoStatus(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
size_t max_serialized_size_lovo_interfaces__msg__LovoStatus(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
bool cdr_serialize_key_lovo_interfaces__msg__LovoStatus(
  const lovo_interfaces__msg__LovoStatus * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
size_t get_serialized_size_key_lovo_interfaces__msg__LovoStatus(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
size_t max_serialized_size_key_lovo_interfaces__msg__LovoStatus(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_lovo_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, lovo_interfaces, msg, LovoStatus)();

#ifdef __cplusplus
}
#endif

#endif  // LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
