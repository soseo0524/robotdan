// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

#include "lovo_interfaces/msg/detail/lovo_status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
const rosidl_type_hash_t *
lovo_interfaces__msg__LovoStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x2e, 0x10, 0x75, 0xde, 0x2a, 0x91, 0xce, 0xb5,
      0x7f, 0x09, 0x8a, 0xdb, 0xe0, 0x38, 0xae, 0x81,
      0xeb, 0xab, 0x38, 0x45, 0x5a, 0x61, 0xdc, 0x7e,
      0x83, 0x8f, 0xd1, 0x29, 0x3f, 0xe8, 0x24, 0xa0,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char lovo_interfaces__msg__LovoStatus__TYPE_NAME[] = "lovo_interfaces/msg/LovoStatus";

// Define type names, field names, and default values
static char lovo_interfaces__msg__LovoStatus__FIELD_NAME__work_id[] = "work_id";
static char lovo_interfaces__msg__LovoStatus__FIELD_NAME__status[] = "status";
static char lovo_interfaces__msg__LovoStatus__FIELD_NAME__message[] = "message";

static rosidl_runtime_c__type_description__Field lovo_interfaces__msg__LovoStatus__FIELDS[] = {
  {
    {lovo_interfaces__msg__LovoStatus__FIELD_NAME__work_id, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT64,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {lovo_interfaces__msg__LovoStatus__FIELD_NAME__status, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {lovo_interfaces__msg__LovoStatus__FIELD_NAME__message, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
lovo_interfaces__msg__LovoStatus__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {lovo_interfaces__msg__LovoStatus__TYPE_NAME, 30, 30},
      {lovo_interfaces__msg__LovoStatus__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int64 work_id\n"
  "string status\n"
  "string message";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
lovo_interfaces__msg__LovoStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {lovo_interfaces__msg__LovoStatus__TYPE_NAME, 30, 30},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 43, 43},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
lovo_interfaces__msg__LovoStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *lovo_interfaces__msg__LovoStatus__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
