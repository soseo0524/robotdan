// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "lovo_interfaces/msg/lovo_status.h"


#ifndef LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__STRUCT_H_
#define LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'status'
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/LovoStatus in the package lovo_interfaces.
typedef struct lovo_interfaces__msg__LovoStatus
{
  int64_t work_id;
  rosidl_runtime_c__String status;
  rosidl_runtime_c__String message;
} lovo_interfaces__msg__LovoStatus;

// Struct for a sequence of lovo_interfaces__msg__LovoStatus.
typedef struct lovo_interfaces__msg__LovoStatus__Sequence
{
  lovo_interfaces__msg__LovoStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lovo_interfaces__msg__LovoStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__STRUCT_H_
