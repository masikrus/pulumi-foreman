# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['ComputeresourceArgs', 'Computeresource']

@pulumi.input_type
class ComputeresourceArgs:
    def __init__(__self__, *,
                 hypervisor: pulumi.Input[str],
                 url: pulumi.Input[str],
                 cachingenabled: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 displaytype: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 setconsolepassword: Optional[pulumi.Input[bool]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Computeresource resource.
        :param pulumi.Input[str] hypervisor: The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
               "Openstack", "Rackspace", "GCE"
        :param pulumi.Input[str] url: URL for Libvirt, oVirt, OpenStack and Rackspace
        :param pulumi.Input[bool] cachingenabled: For VMware only
        :param pulumi.Input[str] datacenter: For oVirt, VMware Datacenter
        :param pulumi.Input[str] description: Description of the compute resource
        :param pulumi.Input[str] displaytype: For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
        :param pulumi.Input[str] name: Name of the compute resource
        :param pulumi.Input[str] password: Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
        :param pulumi.Input[str] server: For VMware
        :param pulumi.Input[bool] setconsolepassword: For Libvirt and VMware only
        :param pulumi.Input[str] user: Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
        """
        pulumi.set(__self__, "hypervisor", hypervisor)
        pulumi.set(__self__, "url", url)
        if cachingenabled is not None:
            pulumi.set(__self__, "cachingenabled", cachingenabled)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if displaytype is not None:
            pulumi.set(__self__, "displaytype", displaytype)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if server is not None:
            pulumi.set(__self__, "server", server)
        if setconsolepassword is not None:
            pulumi.set(__self__, "setconsolepassword", setconsolepassword)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def hypervisor(self) -> pulumi.Input[str]:
        """
        The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
        "Openstack", "Rackspace", "GCE"
        """
        return pulumi.get(self, "hypervisor")

    @hypervisor.setter
    def hypervisor(self, value: pulumi.Input[str]):
        pulumi.set(self, "hypervisor", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL for Libvirt, oVirt, OpenStack and Rackspace
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def cachingenabled(self) -> Optional[pulumi.Input[bool]]:
        """
        For VMware only
        """
        return pulumi.get(self, "cachingenabled")

    @cachingenabled.setter
    def cachingenabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cachingenabled", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        For oVirt, VMware Datacenter
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the compute resource
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def displaytype(self) -> Optional[pulumi.Input[str]]:
        """
        For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
        """
        return pulumi.get(self, "displaytype")

    @displaytype.setter
    def displaytype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "displaytype", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the compute resource
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[str]]:
        """
        For VMware
        """
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server", value)

    @property
    @pulumi.getter
    def setconsolepassword(self) -> Optional[pulumi.Input[bool]]:
        """
        For Libvirt and VMware only
        """
        return pulumi.get(self, "setconsolepassword")

    @setconsolepassword.setter
    def setconsolepassword(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "setconsolepassword", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


@pulumi.input_type
class _ComputeresourceState:
    def __init__(__self__, *,
                 __meta_: Optional[pulumi.Input[bool]] = None,
                 cachingenabled: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 displaytype: Optional[pulumi.Input[str]] = None,
                 hypervisor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 setconsolepassword: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Computeresource resources.
        :param pulumi.Input[bool] __meta_: @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
               autonomy, authority, or control for a portion of a network.
        :param pulumi.Input[bool] cachingenabled: For VMware only
        :param pulumi.Input[str] datacenter: For oVirt, VMware Datacenter
        :param pulumi.Input[str] description: Description of the compute resource
        :param pulumi.Input[str] displaytype: For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
        :param pulumi.Input[str] hypervisor: The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
               "Openstack", "Rackspace", "GCE"
        :param pulumi.Input[str] name: Name of the compute resource
        :param pulumi.Input[str] password: Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
        :param pulumi.Input[str] server: For VMware
        :param pulumi.Input[bool] setconsolepassword: For Libvirt and VMware only
        :param pulumi.Input[str] url: URL for Libvirt, oVirt, OpenStack and Rackspace
        :param pulumi.Input[str] user: Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
        """
        if __meta_ is not None:
            pulumi.set(__self__, "__meta_", __meta_)
        if cachingenabled is not None:
            pulumi.set(__self__, "cachingenabled", cachingenabled)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if displaytype is not None:
            pulumi.set(__self__, "displaytype", displaytype)
        if hypervisor is not None:
            pulumi.set(__self__, "hypervisor", hypervisor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if server is not None:
            pulumi.set(__self__, "server", server)
        if setconsolepassword is not None:
            pulumi.set(__self__, "setconsolepassword", setconsolepassword)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def __meta_(self) -> Optional[pulumi.Input[bool]]:
        """
        @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
        autonomy, authority, or control for a portion of a network.
        """
        return pulumi.get(self, "__meta_")

    @__meta_.setter
    def __meta_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "__meta_", value)

    @property
    @pulumi.getter
    def cachingenabled(self) -> Optional[pulumi.Input[bool]]:
        """
        For VMware only
        """
        return pulumi.get(self, "cachingenabled")

    @cachingenabled.setter
    def cachingenabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cachingenabled", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        For oVirt, VMware Datacenter
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the compute resource
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def displaytype(self) -> Optional[pulumi.Input[str]]:
        """
        For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
        """
        return pulumi.get(self, "displaytype")

    @displaytype.setter
    def displaytype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "displaytype", value)

    @property
    @pulumi.getter
    def hypervisor(self) -> Optional[pulumi.Input[str]]:
        """
        The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
        "Openstack", "Rackspace", "GCE"
        """
        return pulumi.get(self, "hypervisor")

    @hypervisor.setter
    def hypervisor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hypervisor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the compute resource
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[str]]:
        """
        For VMware
        """
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server", value)

    @property
    @pulumi.getter
    def setconsolepassword(self) -> Optional[pulumi.Input[bool]]:
        """
        For Libvirt and VMware only
        """
        return pulumi.get(self, "setconsolepassword")

    @setconsolepassword.setter
    def setconsolepassword(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "setconsolepassword", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL for Libvirt, oVirt, OpenStack and Rackspace
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class Computeresource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cachingenabled: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 displaytype: Optional[pulumi.Input[str]] = None,
                 hypervisor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 setconsolepassword: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Computeresource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cachingenabled: For VMware only
        :param pulumi.Input[str] datacenter: For oVirt, VMware Datacenter
        :param pulumi.Input[str] description: Description of the compute resource
        :param pulumi.Input[str] displaytype: For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
        :param pulumi.Input[str] hypervisor: The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
               "Openstack", "Rackspace", "GCE"
        :param pulumi.Input[str] name: Name of the compute resource
        :param pulumi.Input[str] password: Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
        :param pulumi.Input[str] server: For VMware
        :param pulumi.Input[bool] setconsolepassword: For Libvirt and VMware only
        :param pulumi.Input[str] url: URL for Libvirt, oVirt, OpenStack and Rackspace
        :param pulumi.Input[str] user: Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComputeresourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Computeresource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComputeresourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComputeresourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cachingenabled: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 displaytype: Optional[pulumi.Input[str]] = None,
                 hypervisor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 setconsolepassword: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComputeresourceArgs.__new__(ComputeresourceArgs)

            __props__.__dict__["cachingenabled"] = cachingenabled
            __props__.__dict__["datacenter"] = datacenter
            __props__.__dict__["description"] = description
            __props__.__dict__["displaytype"] = displaytype
            if hypervisor is None and not opts.urn:
                raise TypeError("Missing required property 'hypervisor'")
            __props__.__dict__["hypervisor"] = hypervisor
            __props__.__dict__["name"] = name
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["server"] = server
            __props__.__dict__["setconsolepassword"] = setconsolepassword
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["user"] = user
            __props__.__dict__["__meta_"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Computeresource, __self__).__init__(
            'foreman:index/computeresource:Computeresource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            __meta_: Optional[pulumi.Input[bool]] = None,
            cachingenabled: Optional[pulumi.Input[bool]] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            displaytype: Optional[pulumi.Input[str]] = None,
            hypervisor: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            server: Optional[pulumi.Input[str]] = None,
            setconsolepassword: Optional[pulumi.Input[bool]] = None,
            url: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'Computeresource':
        """
        Get an existing Computeresource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] __meta_: @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
               autonomy, authority, or control for a portion of a network.
        :param pulumi.Input[bool] cachingenabled: For VMware only
        :param pulumi.Input[str] datacenter: For oVirt, VMware Datacenter
        :param pulumi.Input[str] description: Description of the compute resource
        :param pulumi.Input[str] displaytype: For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
        :param pulumi.Input[str] hypervisor: The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
               "Openstack", "Rackspace", "GCE"
        :param pulumi.Input[str] name: Name of the compute resource
        :param pulumi.Input[str] password: Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
        :param pulumi.Input[str] server: For VMware
        :param pulumi.Input[bool] setconsolepassword: For Libvirt and VMware only
        :param pulumi.Input[str] url: URL for Libvirt, oVirt, OpenStack and Rackspace
        :param pulumi.Input[str] user: Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComputeresourceState.__new__(_ComputeresourceState)

        __props__.__dict__["__meta_"] = __meta_
        __props__.__dict__["cachingenabled"] = cachingenabled
        __props__.__dict__["datacenter"] = datacenter
        __props__.__dict__["description"] = description
        __props__.__dict__["displaytype"] = displaytype
        __props__.__dict__["hypervisor"] = hypervisor
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["server"] = server
        __props__.__dict__["setconsolepassword"] = setconsolepassword
        __props__.__dict__["url"] = url
        __props__.__dict__["user"] = user
        return Computeresource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def __meta_(self) -> pulumi.Output[bool]:
        """
        @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
        autonomy, authority, or control for a portion of a network.
        """
        return pulumi.get(self, "__meta_")

    @property
    @pulumi.getter
    def cachingenabled(self) -> pulumi.Output[Optional[bool]]:
        """
        For VMware only
        """
        return pulumi.get(self, "cachingenabled")

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[Optional[str]]:
        """
        For oVirt, VMware Datacenter
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the compute resource
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def displaytype(self) -> pulumi.Output[Optional[str]]:
        """
        For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
        """
        return pulumi.get(self, "displaytype")

    @property
    @pulumi.getter
    def hypervisor(self) -> pulumi.Output[str]:
        """
        The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
        "Openstack", "Rackspace", "GCE"
        """
        return pulumi.get(self, "hypervisor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the compute resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def server(self) -> pulumi.Output[Optional[str]]:
        """
        For VMware
        """
        return pulumi.get(self, "server")

    @property
    @pulumi.getter
    def setconsolepassword(self) -> pulumi.Output[Optional[bool]]:
        """
        For Libvirt and VMware only
        """
        return pulumi.get(self, "setconsolepassword")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        URL for Libvirt, oVirt, OpenStack and Rackspace
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[str]]:
        """
        Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
        """
        return pulumi.get(self, "user")

