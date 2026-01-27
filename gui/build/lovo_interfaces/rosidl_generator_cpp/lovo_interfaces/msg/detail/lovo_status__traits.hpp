// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "lovo_interfaces/msg/lovo_status.hpp"


#ifndef LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__TRAITS_HPP_
#define LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "lovo_interfaces/msg/detail/lovo_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace lovo_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const LovoStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: work_id
  {
    out << "work_id: ";
    rosidl_generator_traits::value_to_yaml(msg.work_id, out);
    out << ", ";
  }

  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LovoStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: work_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "work_id: ";
    rosidl_generator_traits::value_to_yaml(msg.work_id, out);
    out << "\n";
  }

  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LovoStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace lovo_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use lovo_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const lovo_interfaces::msg::LovoStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  lovo_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use lovo_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const lovo_interfaces::msg::LovoStatus & msg)
{
  return lovo_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<lovo_interfaces::msg::LovoStatus>()
{
  return "lovo_interfaces::msg::LovoStatus";
}

template<>
inline const char * name<lovo_interfaces::msg::LovoStatus>()
{
  return "lovo_interfaces/msg/LovoStatus";
}

template<>
struct has_fixed_size<lovo_interfaces::msg::LovoStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<lovo_interfaces::msg::LovoStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<lovo_interfaces::msg::LovoStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__TRAITS_HPP_
