// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from lovo_interfaces:msg/LovoStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "lovo_interfaces/msg/lovo_status.hpp"


#ifndef LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__STRUCT_HPP_
#define LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__lovo_interfaces__msg__LovoStatus __attribute__((deprecated))
#else
# define DEPRECATED__lovo_interfaces__msg__LovoStatus __declspec(deprecated)
#endif

namespace lovo_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LovoStatus_
{
  using Type = LovoStatus_<ContainerAllocator>;

  explicit LovoStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->work_id = 0ll;
      this->status = "";
      this->message = "";
    }
  }

  explicit LovoStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : status(_alloc),
    message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->work_id = 0ll;
      this->status = "";
      this->message = "";
    }
  }

  // field types and members
  using _work_id_type =
    int64_t;
  _work_id_type work_id;
  using _status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _status_type status;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__work_id(
    const int64_t & _arg)
  {
    this->work_id = _arg;
    return *this;
  }
  Type & set__status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    lovo_interfaces::msg::LovoStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const lovo_interfaces::msg::LovoStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      lovo_interfaces::msg::LovoStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      lovo_interfaces::msg::LovoStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__lovo_interfaces__msg__LovoStatus
    std::shared_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__lovo_interfaces__msg__LovoStatus
    std::shared_ptr<lovo_interfaces::msg::LovoStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LovoStatus_ & other) const
  {
    if (this->work_id != other.work_id) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const LovoStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LovoStatus_

// alias to use template instance with default allocator
using LovoStatus =
  lovo_interfaces::msg::LovoStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace lovo_interfaces

#endif  // LOVO_INTERFACES__MSG__DETAIL__LOVO_STATUS__STRUCT_HPP_
