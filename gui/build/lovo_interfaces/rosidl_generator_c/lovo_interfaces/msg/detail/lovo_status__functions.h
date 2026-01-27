// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "lovo_interfaces/msg/lovo_status.h"


#ifndef LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__FUNCTIONS_H_
#define LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_runtime_c/type_description/type_description__struct.h"
#include "rosidl_runtime_c/type_description/type_source__struct.h"
#include "rosidl_runtime_c/type_hash.h"
#include "rosidl_runtime_c/visibility_control.h"
#include "lovo_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "lovo_interfaces/msg/detail/lovo_status__struct.h"

/// Initialize msg/LovoStatus message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * lovo_interfaces__msg__LovoStatus
 * )) before or use
 * lovo_interfaces__msg__LovoStatus__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
bool
lovo_interfaces__msg__LovoStatus__init(lovo_interfaces__msg__LovoStatus * msg);

/// Finalize msg/LovoStatus message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
void
lovo_interfaces__msg__LovoStatus__fini(lovo_interfaces__msg__LovoStatus * msg);

/// Create msg/LovoStatus message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * lovo_interfaces__msg__LovoStatus__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
lovo_interfaces__msg__LovoStatus *
lovo_interfaces__msg__LovoStatus__create(void);

/// Destroy msg/LovoStatus message.
/**
 * It calls
 * lovo_interfaces__msg__LovoStatus__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
void
lovo_interfaces__msg__LovoStatus__destroy(lovo_interfaces__msg__LovoStatus * msg);

/// Check for msg/LovoStatus message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
bool
lovo_interfaces__msg__LovoStatus__are_equal(const lovo_interfaces__msg__LovoStatus * lhs, const lovo_interfaces__msg__LovoStatus * rhs);

/// Copy a msg/LovoStatus message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
bool
lovo_interfaces__msg__LovoStatus__copy(
  const lovo_interfaces__msg__LovoStatus * input,
  lovo_interfaces__msg__LovoStatus * output);

/// Retrieve pointer to the hash of the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
const rosidl_type_hash_t *
lovo_interfaces__msg__LovoStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
const rosidl_runtime_c__type_description__TypeDescription *
lovo_interfaces__msg__LovoStatus__get_type_description(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the single raw source text that defined this type.
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
const rosidl_runtime_c__type_description__TypeSource *
lovo_interfaces__msg__LovoStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the recursive raw sources that defined the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
const rosidl_runtime_c__type_description__TypeSource__Sequence *
lovo_interfaces__msg__LovoStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support);

/// Initialize array of msg/LovoStatus messages.
/**
 * It allocates the memory for the number of elements and calls
 * lovo_interfaces__msg__LovoStatus__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
bool
lovo_interfaces__msg__LovoStatus__Sequence__init(lovo_interfaces__msg__LovoStatus__Sequence * array, size_t size);

/// Finalize array of msg/LovoStatus messages.
/**
 * It calls
 * lovo_interfaces__msg__LovoStatus__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
void
lovo_interfaces__msg__LovoStatus__Sequence__fini(lovo_interfaces__msg__LovoStatus__Sequence * array);

/// Create array of msg/LovoStatus messages.
/**
 * It allocates the memory for the array and calls
 * lovo_interfaces__msg__LovoStatus__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
lovo_interfaces__msg__LovoStatus__Sequence *
lovo_interfaces__msg__LovoStatus__Sequence__create(size_t size);

/// Destroy array of msg/LovoStatus messages.
/**
 * It calls
 * lovo_interfaces__msg__LovoStatus__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
void
lovo_interfaces__msg__LovoStatus__Sequence__destroy(lovo_interfaces__msg__LovoStatus__Sequence * array);

/// Check for msg/LovoStatus message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
bool
lovo_interfaces__msg__LovoStatus__Sequence__are_equal(const lovo_interfaces__msg__LovoStatus__Sequence * lhs, const lovo_interfaces__msg__LovoStatus__Sequence * rhs);

/// Copy an array of msg/LovoStatus messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_lovo_interfaces
bool
lovo_interfaces__msg__LovoStatus__Sequence__copy(
  const lovo_interfaces__msg__LovoStatus__Sequence * input,
  lovo_interfaces__msg__LovoStatus__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__FUNCTIONS_H_
