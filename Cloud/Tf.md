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
