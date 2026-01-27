// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "lovo_interfaces/msg/detail/lovo_status__rosidl_typesupport_introspection_c.h"
#include "lovo_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "lovo_interfaces/msg/detail/lovo_status__functions.h"
#include "lovo_interfaces/msg/detail/lovo_status__struct.h"


// Include directives for member types
// Member `status`
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  lovo_interfaces__msg__LovoStatus__init(message_memory);
}

void lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_fini_function(void * message_memory)
{
  lovo_interfaces__msg__LovoStatus__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_member_array[3] = {
  {
    "work_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lovo_interfaces__msg__LovoStatus, work_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lovo_interfaces__msg__LovoStatus, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lovo_interfaces__msg__LovoStatus, message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_members = {
  "lovo_interfaces__msg",  // message namespace
  "LovoStatus",  // message name
  3,  // number of fields
  sizeof(lovo_interfaces__msg__LovoStatus),
  false,  // has_any_key_member_
  lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_member_array,  // message members
  lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_type_support_handle = {
  0,
  &lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_members,
  get_message_typesupport_handle_function,
  &lovo_interfaces__msg__LovoStatus__get_type_hash,
  &lovo_interfaces__msg__LovoStatus__get_type_description,
  &lovo_interfaces__msg__LovoStatus__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_lovo_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lovo_interfaces, msg, LovoStatus)() {
  if (!lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_type_support_handle.typesupport_identifier) {
    lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &lovo_interfaces__msg__LovoStatus__rosidl_typesupport_introspection_c__LovoStatus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
