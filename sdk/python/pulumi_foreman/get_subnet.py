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

__all__ = [
    'GetSubnetResult',
    'AwaitableGetSubnetResult',
    'get_subnet',
    'get_subnet_output',
]

@pulumi.output_type
class GetSubnetResult:
    """
    A collection of values returned by getSubnet.
    """
    def __init__(__self__, bmc_id=None, boot_mode=None, description=None, dhcp_id=None, dns_primary=None, dns_secondary=None, domain_ids=None, from_=None, gateway=None, httpboot_id=None, id=None, ipam=None, mask=None, mtu=None, name=None, network=None, network_address=None, network_type=None, template_id=None, tftp_id=None, to=None, vlanid=None):
        if bmc_id and not isinstance(bmc_id, int):
            raise TypeError("Expected argument 'bmc_id' to be a int")
        pulumi.set(__self__, "bmc_id", bmc_id)
        if boot_mode and not isinstance(boot_mode, str):
            raise TypeError("Expected argument 'boot_mode' to be a str")
        pulumi.set(__self__, "boot_mode", boot_mode)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dhcp_id and not isinstance(dhcp_id, int):
            raise TypeError("Expected argument 'dhcp_id' to be a int")
        pulumi.set(__self__, "dhcp_id", dhcp_id)
        if dns_primary and not isinstance(dns_primary, str):
            raise TypeError("Expected argument 'dns_primary' to be a str")
        pulumi.set(__self__, "dns_primary", dns_primary)
        if dns_secondary and not isinstance(dns_secondary, str):
            raise TypeError("Expected argument 'dns_secondary' to be a str")
        pulumi.set(__self__, "dns_secondary", dns_secondary)
        if domain_ids and not isinstance(domain_ids, list):
            raise TypeError("Expected argument 'domain_ids' to be a list")
        pulumi.set(__self__, "domain_ids", domain_ids)
        if from_ and not isinstance(from_, str):
            raise TypeError("Expected argument 'from_' to be a str")
        pulumi.set(__self__, "from_", from_)
        if gateway and not isinstance(gateway, str):
            raise TypeError("Expected argument 'gateway' to be a str")
        pulumi.set(__self__, "gateway", gateway)
        if httpboot_id and not isinstance(httpboot_id, int):
            raise TypeError("Expected argument 'httpboot_id' to be a int")
        pulumi.set(__self__, "httpboot_id", httpboot_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipam and not isinstance(ipam, str):
            raise TypeError("Expected argument 'ipam' to be a str")
        pulumi.set(__self__, "ipam", ipam)
        if mask and not isinstance(mask, str):
            raise TypeError("Expected argument 'mask' to be a str")
        pulumi.set(__self__, "mask", mask)
        if mtu and not isinstance(mtu, int):
            raise TypeError("Expected argument 'mtu' to be a int")
        pulumi.set(__self__, "mtu", mtu)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if network_address and not isinstance(network_address, str):
            raise TypeError("Expected argument 'network_address' to be a str")
        pulumi.set(__self__, "network_address", network_address)
        if network_type and not isinstance(network_type, str):
            raise TypeError("Expected argument 'network_type' to be a str")
        pulumi.set(__self__, "network_type", network_type)
        if template_id and not isinstance(template_id, int):
            raise TypeError("Expected argument 'template_id' to be a int")
        pulumi.set(__self__, "template_id", template_id)
        if tftp_id and not isinstance(tftp_id, int):
            raise TypeError("Expected argument 'tftp_id' to be a int")
        pulumi.set(__self__, "tftp_id", tftp_id)
        if to and not isinstance(to, str):
            raise TypeError("Expected argument 'to' to be a str")
        pulumi.set(__self__, "to", to)
        if vlanid and not isinstance(vlanid, int):
            raise TypeError("Expected argument 'vlanid' to be a int")
        pulumi.set(__self__, "vlanid", vlanid)

    @property
    @pulumi.getter(name="bmcId")
    def bmc_id(self) -> int:
        return pulumi.get(self, "bmc_id")

    @property
    @pulumi.getter(name="bootMode")
    def boot_mode(self) -> str:
        return pulumi.get(self, "boot_mode")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dhcpId")
    def dhcp_id(self) -> int:
        return pulumi.get(self, "dhcp_id")

    @property
    @pulumi.getter(name="dnsPrimary")
    def dns_primary(self) -> str:
        return pulumi.get(self, "dns_primary")

    @property
    @pulumi.getter(name="dnsSecondary")
    def dns_secondary(self) -> str:
        return pulumi.get(self, "dns_secondary")

    @property
    @pulumi.getter(name="domainIds")
    def domain_ids(self) -> Sequence[int]:
        return pulumi.get(self, "domain_ids")

    @property
    @pulumi.getter(name="from")
    def from_(self) -> str:
        return pulumi.get(self, "from_")

    @property
    @pulumi.getter
    def gateway(self) -> str:
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="httpbootId")
    def httpboot_id(self) -> int:
        return pulumi.get(self, "httpboot_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ipam(self) -> str:
        return pulumi.get(self, "ipam")

    @property
    @pulumi.getter
    def mask(self) -> str:
        return pulumi.get(self, "mask")

    @property
    @pulumi.getter
    def mtu(self) -> int:
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> Optional[str]:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkAddress")
    def network_address(self) -> str:
        return pulumi.get(self, "network_address")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> str:
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> int:
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter(name="tftpId")
    def tftp_id(self) -> int:
        return pulumi.get(self, "tftp_id")

    @property
    @pulumi.getter
    def to(self) -> str:
        return pulumi.get(self, "to")

    @property
    @pulumi.getter
    def vlanid(self) -> int:
        return pulumi.get(self, "vlanid")


class AwaitableGetSubnetResult(GetSubnetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubnetResult(
            bmc_id=self.bmc_id,
            boot_mode=self.boot_mode,
            description=self.description,
            dhcp_id=self.dhcp_id,
            dns_primary=self.dns_primary,
            dns_secondary=self.dns_secondary,
            domain_ids=self.domain_ids,
            from_=self.from_,
            gateway=self.gateway,
            httpboot_id=self.httpboot_id,
            id=self.id,
            ipam=self.ipam,
            mask=self.mask,
            mtu=self.mtu,
            name=self.name,
            network=self.network,
            network_address=self.network_address,
            network_type=self.network_type,
            template_id=self.template_id,
            tftp_id=self.tftp_id,
            to=self.to,
            vlanid=self.vlanid)


def get_subnet(name: Optional[str] = None,
               network: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubnetResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['network'] = network
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getSubnet:getSubnet', __args__, opts=opts, typ=GetSubnetResult).value

    return AwaitableGetSubnetResult(
        bmc_id=pulumi.get(__ret__, 'bmc_id'),
        boot_mode=pulumi.get(__ret__, 'boot_mode'),
        description=pulumi.get(__ret__, 'description'),
        dhcp_id=pulumi.get(__ret__, 'dhcp_id'),
        dns_primary=pulumi.get(__ret__, 'dns_primary'),
        dns_secondary=pulumi.get(__ret__, 'dns_secondary'),
        domain_ids=pulumi.get(__ret__, 'domain_ids'),
        from_=pulumi.get(__ret__, 'from_'),
        gateway=pulumi.get(__ret__, 'gateway'),
        httpboot_id=pulumi.get(__ret__, 'httpboot_id'),
        id=pulumi.get(__ret__, 'id'),
        ipam=pulumi.get(__ret__, 'ipam'),
        mask=pulumi.get(__ret__, 'mask'),
        mtu=pulumi.get(__ret__, 'mtu'),
        name=pulumi.get(__ret__, 'name'),
        network=pulumi.get(__ret__, 'network'),
        network_address=pulumi.get(__ret__, 'network_address'),
        network_type=pulumi.get(__ret__, 'network_type'),
        template_id=pulumi.get(__ret__, 'template_id'),
        tftp_id=pulumi.get(__ret__, 'tftp_id'),
        to=pulumi.get(__ret__, 'to'),
        vlanid=pulumi.get(__ret__, 'vlanid'))
def get_subnet_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                      network: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSubnetResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['network'] = network
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getSubnet:getSubnet', __args__, opts=opts, typ=GetSubnetResult)
    return __ret__.apply(lambda __response__: GetSubnetResult(
        bmc_id=pulumi.get(__response__, 'bmc_id'),
        boot_mode=pulumi.get(__response__, 'boot_mode'),
        description=pulumi.get(__response__, 'description'),
        dhcp_id=pulumi.get(__response__, 'dhcp_id'),
        dns_primary=pulumi.get(__response__, 'dns_primary'),
        dns_secondary=pulumi.get(__response__, 'dns_secondary'),
        domain_ids=pulumi.get(__response__, 'domain_ids'),
        from_=pulumi.get(__response__, 'from_'),
        gateway=pulumi.get(__response__, 'gateway'),
        httpboot_id=pulumi.get(__response__, 'httpboot_id'),
        id=pulumi.get(__response__, 'id'),
        ipam=pulumi.get(__response__, 'ipam'),
        mask=pulumi.get(__response__, 'mask'),
        mtu=pulumi.get(__response__, 'mtu'),
        name=pulumi.get(__response__, 'name'),
        network=pulumi.get(__response__, 'network'),
        network_address=pulumi.get(__response__, 'network_address'),
        network_type=pulumi.get(__response__, 'network_type'),
        template_id=pulumi.get(__response__, 'template_id'),
        tftp_id=pulumi.get(__response__, 'tftp_id'),
        to=pulumi.get(__response__, 'to'),
        vlanid=pulumi.get(__response__, 'vlanid')))
