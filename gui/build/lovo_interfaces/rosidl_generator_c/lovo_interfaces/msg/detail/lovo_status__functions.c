// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice
#include "lovo_interfaces/msg/detail/lovo_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `status`
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

bool
lovo_interfaces__msg__LovoStatus__init(lovo_interfaces__msg__LovoStatus * msg)
{
  if (!msg) {
    return false;
  }
  // work_id
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    lovo_interfaces__msg__LovoStatus__fini(msg);
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    lovo_interfaces__msg__LovoStatus__fini(msg);
    return false;
  }
  return true;
}

void
lovo_interfaces__msg__LovoStatus__fini(lovo_interfaces__msg__LovoStatus * msg)
{
  if (!msg) {
    return;
  }
  // work_id
  // status
  rosidl_runtime_c__String__fini(&msg->status);
  // message
  rosidl_runtime_c__String__fini(&msg->message);
}

bool
lovo_interfaces__msg__LovoStatus__are_equal(const lovo_interfaces__msg__LovoStatus * lhs, const lovo_interfaces__msg__LovoStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // work_id
  if (lhs->work_id != rhs->work_id) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  return true;
}

bool
lovo_interfaces__msg__LovoStatus__copy(
  const lovo_interfaces__msg__LovoStatus * input,
  lovo_interfaces__msg__LovoStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // work_id
  output->work_id = input->work_id;
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  return true;
}

lovo_interfaces__msg__LovoStatus *
lovo_interfaces__msg__LovoStatus__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lovo_interfaces__msg__LovoStatus * msg = (lovo_interfaces__msg__LovoStatus *)allocator.allocate(sizeof(lovo_interfaces__msg__LovoStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(lovo_interfaces__msg__LovoStatus));
  bool success = lovo_interfaces__msg__LovoStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
lovo_interfaces__msg__LovoStatus__destroy(lovo_interfaces__msg__LovoStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    lovo_interfaces__msg__LovoStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
lovo_interfaces__msg__LovoStatus__Sequence__init(lovo_interfaces__msg__LovoStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lovo_interfaces__msg__LovoStatus * data = NULL;

  if (size) {
    data = (lovo_interfaces__msg__LovoStatus *)allocator.zero_allocate(size, sizeof(lovo_interfaces__msg__LovoStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = lovo_interfaces__msg__LovoStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        lovo_interfaces__msg__LovoStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
lovo_interfaces__msg__LovoStatus__Sequence__fini(lovo_interfaces__msg__LovoStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      lovo_interfaces__msg__LovoStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

lovo_interfaces__msg__LovoStatus__Sequence *
lovo_interfaces__msg__LovoStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lovo_interfaces__msg__LovoStatus__Sequence * array = (lovo_interfaces__msg__LovoStatus__Sequence *)allocator.allocate(sizeof(lovo_interfaces__msg__LovoStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = lovo_interfaces__msg__LovoStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
lovo_interfaces__msg__LovoStatus__Sequence__destroy(lovo_interfaces__msg__LovoStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    lovo_interfaces__msg__LovoStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
lovo_interfaces__msg__LovoStatus__Sequence__are_equal(const lovo_interfaces__msg__LovoStatus__Sequence * lhs, const lovo_interfaces__msg__LovoStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!lovo_interfaces__msg__LovoStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
lovo_interfaces__msg__LovoStatus__Sequence__copy(
  const lovo_interfaces__msg__LovoStatus__Sequence * input,
  lovo_interfaces__msg__LovoStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(lovo_interfaces__msg__LovoStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    lovo_interfaces__msg__LovoStatus * data =
      (lovo_interfaces__msg__LovoStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!lovo_interfaces__msg__LovoStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          lovo_interfaces__msg__LovoStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!lovo_interfaces__msg__LovoStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
