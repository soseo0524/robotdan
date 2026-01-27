// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "lovo_interfaces/msg/detail/lovo_status__functions.h"
#include "lovo_interfaces/msg/detail/lovo_status__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace lovo_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void LovoStatus_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) lovo_interfaces::msg::LovoStatus(_init);
}

void LovoStatus_fini_function(void * message_memory)
{
  auto typed_message = static_cast<lovo_interfaces::msg::LovoStatus *>(message_memory);
  typed_message->~LovoStatus();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember LovoStatus_message_member_array[3] = {
  {
    "work_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lovo_interfaces::msg::LovoStatus, work_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lovo_interfaces::msg::LovoStatus, status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "message",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lovo_interfaces::msg::LovoStatus, message),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers LovoStatus_message_members = {
  "lovo_interfaces::msg",  // message namespace
  "LovoStatus",  // message name
  3,  // number of fields
  sizeof(lovo_interfaces::msg::LovoStatus),
  false,  // has_any_key_member_
  LovoStatus_message_member_array,  // message members
  LovoStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  LovoStatus_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t LovoStatus_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &LovoStatus_message_members,
  get_message_typesupport_handle_function,
  &lovo_interfaces__msg__LovoStatus__get_type_hash,
  &lovo_interfaces__msg__LovoStatus__get_type_description,
  &lovo_interfaces__msg__LovoStatus__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace lovo_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<lovo_interfaces::msg::LovoStatus>()
{
  return &::lovo_interfaces::msg::rosidl_typesupport_introspection_cpp::LovoStatus_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, lovo_interfaces, msg, LovoStatus)() {
  return &::lovo_interfaces::msg::rosidl_typesupport_introspection_cpp::LovoStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
