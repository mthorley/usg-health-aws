
# --------------------------------------------
# Credentials
# --------------------------------------------

# aws prod account
variable "prod_access_key" {}
variable "prod_secret_key" {}

# ---------------------------------------------
# Networking
# - VPC contains only two subnets at present
# ---------------------------------------------
# aws vpc and subnet config
variable "vpc_cidr" {}
variable "sn1_cidr" {}
variable "sn2_cidr" {}
variable "pub_sn_cidr" {}

# env - e.g. prodA, devA
variable "env" {}
