variable "region" {
  default = "eu-north-1"
}

variable "app_name" {
  default = "counter-service"
}

variable "eks_instance_type" {
  default = "t3.small"
}

variable "eks_asg_desired_capacity" {
  default = 1
}

variable "eks_asg_min_capacity" {
  default = 1
}

variable "eks_asg_max_capacity" {
  default = 3
}