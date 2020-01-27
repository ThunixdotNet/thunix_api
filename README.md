# Thunix API

This is the working spec for the Thunix API.  Until finalization, the spec will be consider v1.  v1 of the API shall be considered unstable, and a work in progress.  The API should be agnostic to linux distros, and flavors of \*Nix OS's (ie, BSD, etc) whenever possible.

The API will be authenticated, at all times, using the user's credentials sent in the host headers.

The API shall return a 200 for successful requests, with the JSON paylod.

The API shall return a 400 for any endpoint not existent.

The API shall return a 401 for unauthenticated requests to endpoints requiring authentication.

The API shall return a 403 for requests which are authenticated, but not permissible for the authenticated user.

The API shall return a 418 for requests to the "/teapot" endpoint.

The API shall return a 420 for requests exceeding the rate limits.

The API shall return a 501 for requests which exist in the spec, but have not been implmented yet.


## API Format

The API is a RESTful API, and the following URIs will be used:

```
https://{hostname}/api/1/{action}
```


## Informational APIs

### ip_info

This endpoint shall return a json struct containing interfaces, and IP addresses in CIDR format:


```
{
    "Interfaces":[
        {
            "Name":"eth0",
            "Addresses":[
                "10.0.0.1/32",
                "10.0.1.100/24"
            ]
        },
        {
            "Name":"wg0",
            "Addresses":[
               "192.168.0.1/24"
            ]
        }
    ]
}
```

### uptime

This will return a JSON payload of system uptime:

```
{
   "days":164,
   "hours":16,
   "mins":22,
   "secs":3
}
```

### mem

This will return a JSON payload containing information about the system memory, in bytes:

```
{
   "free" : 8668672000,
   "total" : 33638055936,
   "percent" : 74.2,
   "used" : 22686449664
}
```

### teapot

This shall return a struct, describing the current tea making capabilities of the system:

```
{
   "tea":"available",
   "height":"short",
   "width":"stout
}
```
