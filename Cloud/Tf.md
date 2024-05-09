## What is Terraform null_resource ?

- By the name itself we can see null - which means there won't be any infrastructure created on cloud.
- The reason is there is no terraform state attached to this, due to which you can update your terrafrom file as many times as you want.

```
resource "null_resource" "example" {
    provisioner "local_exec" {
        command = "echo hello world"
    }
}
```

## What is trigger in null_resource ?

- trigger in null_resource will holds key-value pair. But this trigger will execute for the first time, and again it'll execute whenever there is a change in the key-value.
- If the key-value pair is changing every time, so the trigger will execute wheneve you run `terrafrom apply` command.

```
resource "null_resource" "example" {
    triggers = {
        id = time()
    }
    provisioner "local_exec" {
        command = "echo hello world"
    }
}
```

In the above example, time function is just an example in which we always get a different value and due to which the local-exec provisioner gets executed all the time.

## Variables in terraform

- Terraform variables are a way to store values that can be reused throughout your Terraform configuration.

- They allow you to define a value once and reference it in multiple places throughout your configuration, making it easier to manage and update your infrastructure.

```
variable "<your_variable_name>" {
    type = string
}
```

number, string, list, map, set, bool

## Terraform variable loading preference - How do terraform loads variables?

Terraform variable loading preference refers to the order in which Terraform on loads variables when multiple sources specify the same variable.
**Order:**

- Environment variables
- Variable files (files with a .tfvars or terraform.tfvars.json extension)
- From Terraform files (using .tf files)
- From the command line (using the -var flag)

## Terraform locals

- Terraform Locals are only accessible within that functions or within the scope of terraform file.
- Terraform locals can be re-used multiple numbers of times in the terraform configuration file.
- It can reduce the work of updating your terraform configuration at multiple places. With terraform locals you need to update its value once and it should reflect all over the place where it is referred.

```
locals {
    my_local = <value>
}
```

## Terraform outputs

- Terraform output values will be really useful when you want to debug your terraform code. Terraform output values can help you to print the attributes reference(arn, instance_state, outpost_arn, public_ip, public_dns etc) on your console.
- If you don't want to show some values use `sensitive=true`

## for loop

```
variable user_names {
    type = list(string)
    default= ["user1", "user2", "user3"]
}

output "print_name" {
    value = [for name in var.user_name: name]
}
```

## for_each

```
variable user_names {
    type = set(string)
    default= ["user1", "user2", "user3"]
}

output "print_name" {
    for_each - var.user_names
    name = each.value
}
```
