// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "lovo_interfaces/msg/detail/lovo_status__struct.h"
#include "lovo_interfaces/msg/detail/lovo_status__type_support.h"
#include "lovo_interfaces/msg/detail/lovo_status__functions.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace lovo_interfaces
{

namespace msg
{

namespace rosidl_typesupport_c
{

typedef struct _LovoStatus_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _LovoStatus_type_support_ids_t;

static const _LovoStatus_type_support_ids_t _LovoStatus_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _LovoStatus_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _LovoStatus_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _LovoStatus_type_support_symbol_names_t _LovoStatus_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, lovo_interfaces, msg, LovoStatus)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lovo_interfaces, msg, LovoStatus)),
  }
};

typedef struct _LovoStatus_type_support_data_t
{
  void * data[2];
} _LovoStatus_type_support_data_t;

static _LovoStatus_type_support_data_t _LovoStatus_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _LovoStatus_message_typesupport_map = {
  2,
  "lovo_interfaces",
  &_LovoStatus_message_typesupport_ids.typesupport_identifier[0],
  &_LovoStatus_message_typesupport_symbol_names.symbol_name[0],
  &_LovoStatus_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t LovoStatus_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_LovoStatus_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &lovo_interfaces__msg__LovoStatus__get_type_hash,
  &lovo_interfaces__msg__LovoStatus__get_type_description,
  &lovo_interfaces__msg__LovoStatus__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace msg

}  // namespace lovo_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, lovo_interfaces, msg, LovoStatus)() {
  return &::lovo_interfaces::msg::rosidl_typesupport_c::LovoStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
