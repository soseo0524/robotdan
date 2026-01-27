// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "lovo_interfaces/msg/lovo_status.hpp"


#ifndef LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__BUILDER_HPP_
#define LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lovo_interfaces/msg/detail/lovo_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lovo_interfaces
{

namespace msg
{

namespace builder
{

class Init_LovoStatus_message
{
public:
  explicit Init_LovoStatus_message(::lovo_interfaces::msg::LovoStatus & msg)
  : msg_(msg)
  {}
  ::lovo_interfaces::msg::LovoStatus message(::lovo_interfaces::msg::LovoStatus::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lovo_interfaces::msg::LovoStatus msg_;
};

class Init_LovoStatus_status
{
public:
  explicit Init_LovoStatus_status(::lovo_interfaces::msg::LovoStatus & msg)
  : msg_(msg)
  {}
  Init_LovoStatus_message status(::lovo_interfaces::msg::LovoStatus::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_LovoStatus_message(msg_);
  }

private:
  ::lovo_interfaces::msg::LovoStatus msg_;
};

class Init_LovoStatus_work_id
{
public:
  Init_LovoStatus_work_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LovoStatus_status work_id(::lovo_interfaces::msg::LovoStatus::_work_id_type arg)
  {
    msg_.work_id = std::move(arg);
    return Init_LovoStatus_status(msg_);
  }

private:
  ::lovo_interfaces::msg::LovoStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::lovo_interfaces::msg::LovoStatus>()
{
  return lovo_interfaces::msg::builder::Init_LovoStatus_work_id();
}

}  // namespace lovo_interfaces

#endif  // LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__BUILDER_HPP_
