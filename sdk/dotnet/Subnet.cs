// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    [ForemanResourceType("foreman:index/subnet:Subnet")]
    public partial class Subnet : global::Pulumi.CustomResource
    {
        /// <summary>
        /// @SUMMARY Foreman representation of a subnetwork.
        /// </summary>
        [Output("__meta_")]
        public Output<bool> __meta_ { get; private set; } = null!;

        /// <summary>
        /// BMC Proxy ID to use within this subnet
        /// </summary>
        [Output("bmcId")]
        public Output<int?> BmcId { get; private set; } = null!;

        /// <summary>
        /// Default boot mode for instances assigned to this subnet. Values include: `"Static"`, `"DHCP"`.
        /// </summary>
        [Output("bootMode")]
        public Output<string?> BootMode { get; private set; } = null!;

        /// <summary>
        /// Description of the subnet
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// DHCP Proxy ID to use within this subnet
        /// </summary>
        [Output("dhcpId")]
        public Output<int?> DhcpId { get; private set; } = null!;

        /// <summary>
        /// Primary DNS server for this subnet.
        /// </summary>
        [Output("dnsPrimary")]
        public Output<string?> DnsPrimary { get; private set; } = null!;

        /// <summary>
        /// Secondary DNS sever for this subnet.
        /// </summary>
        [Output("dnsSecondary")]
        public Output<string?> DnsSecondary { get; private set; } = null!;

        /// <summary>
        /// Domains in which this subnet is part
        /// </summary>
        [Output("domainIds")]
        public Output<ImmutableArray<int>> DomainIds { get; private set; } = null!;

        /// <summary>
        /// Start IP address for IP auto suggestion.
        /// </summary>
        [Output("from")]
        public Output<string?> From { get; private set; } = null!;

        /// <summary>
        /// Gateway server to use when connecting/communicating to anything not on the same network.
        /// </summary>
        [Output("gateway")]
        public Output<string?> Gateway { get; private set; } = null!;

        /// <summary>
        /// HTTPBoot Proxy ID to use within this subnet
        /// </summary>
        [Output("httpbootId")]
        public Output<int?> HttpbootId { get; private set; } = null!;

        /// <summary>
        /// IP address auto-suggestion for this subnet. Valid values include: `"DHCP"`, `"Internal DB"`, `"Random DB"`,`"None"`.
        /// </summary>
        [Output("ipam")]
        public Output<string?> Ipam { get; private set; } = null!;

        /// <summary>
        /// Netmask for this subnet. @EXAMPLE "255.255.255.0"
        /// </summary>
        [Output("mask")]
        public Output<string> Mask { get; private set; } = null!;

        /// <summary>
        /// MTU value for the subnet
        /// </summary>
        [Output("mtu")]
        public Output<int?> Mtu { get; private set; } = null!;

        /// <summary>
        /// Subnet name. @EXAMPLE "10.228.247.0 BO1"
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Subnet network. @EXAMPLE "10.228.247.0"
        /// </summary>
        [Output("network")]
        public Output<string> Network { get; private set; } = null!;

        /// <summary>
        /// The Subnets CIDR in the format 169.254.0.0/16
        /// </summary>
        [Output("networkAddress")]
        public Output<string?> NetworkAddress { get; private set; } = null!;

        /// <summary>
        /// Type or protocol, IPv4 or IPv6, defaults to IPv4.
        /// </summary>
        [Output("networkType")]
        public Output<string?> NetworkType { get; private set; } = null!;

        /// <summary>
        /// Template HTTP(S) Proxy ID to use within this subnet
        /// </summary>
        [Output("templateId")]
        public Output<int?> TemplateId { get; private set; } = null!;

        /// <summary>
        /// TFTP Proxy ID to use within this subnet
        /// </summary>
        [Output("tftpId")]
        public Output<int?> TftpId { get; private set; } = null!;

        /// <summary>
        /// Ending IP address for IP auto suggestion.
        /// </summary>
        [Output("to")]
        public Output<string?> To { get; private set; } = null!;

        /// <summary>
        /// VLAN id that is in use in the subnet
        /// </summary>
        [Output("vlanid")]
        public Output<int?> Vlanid { get; private set; } = null!;


        /// <summary>
        /// Create a Subnet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Subnet(string name, SubnetArgs args, CustomResourceOptions? options = null)
            : base("foreman:index/subnet:Subnet", name, args ?? new SubnetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Subnet(string name, Input<string> id, SubnetState? state = null, CustomResourceOptions? options = null)
            : base("foreman:index/subnet:Subnet", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Subnet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Subnet Get(string name, Input<string> id, SubnetState? state = null, CustomResourceOptions? options = null)
        {
            return new Subnet(name, id, state, options);
        }
    }

    public sealed class SubnetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// BMC Proxy ID to use within this subnet
        /// </summary>
        [Input("bmcId")]
        public Input<int>? BmcId { get; set; }

        /// <summary>
        /// Default boot mode for instances assigned to this subnet. Values include: `"Static"`, `"DHCP"`.
        /// </summary>
        [Input("bootMode")]
        public Input<string>? BootMode { get; set; }

        /// <summary>
        /// Description of the subnet
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// DHCP Proxy ID to use within this subnet
        /// </summary>
        [Input("dhcpId")]
        public Input<int>? DhcpId { get; set; }

        /// <summary>
        /// Primary DNS server for this subnet.
        /// </summary>
        [Input("dnsPrimary")]
        public Input<string>? DnsPrimary { get; set; }

        /// <summary>
        /// Secondary DNS sever for this subnet.
        /// </summary>
        [Input("dnsSecondary")]
        public Input<string>? DnsSecondary { get; set; }

        [Input("domainIds")]
        private InputList<int>? _domainIds;

        /// <summary>
        /// Domains in which this subnet is part
        /// </summary>
        public InputList<int> DomainIds
        {
            get => _domainIds ?? (_domainIds = new InputList<int>());
            set => _domainIds = value;
        }

        /// <summary>
        /// Start IP address for IP auto suggestion.
        /// </summary>
        [Input("from")]
        public Input<string>? From { get; set; }

        /// <summary>
        /// Gateway server to use when connecting/communicating to anything not on the same network.
        /// </summary>
        [Input("gateway")]
        public Input<string>? Gateway { get; set; }

        /// <summary>
        /// HTTPBoot Proxy ID to use within this subnet
        /// </summary>
        [Input("httpbootId")]
        public Input<int>? HttpbootId { get; set; }

        /// <summary>
        /// IP address auto-suggestion for this subnet. Valid values include: `"DHCP"`, `"Internal DB"`, `"Random DB"`,`"None"`.
        /// </summary>
        [Input("ipam")]
        public Input<string>? Ipam { get; set; }

        /// <summary>
        /// Netmask for this subnet. @EXAMPLE "255.255.255.0"
        /// </summary>
        [Input("mask", required: true)]
        public Input<string> Mask { get; set; } = null!;

        /// <summary>
        /// MTU value for the subnet
        /// </summary>
        [Input("mtu")]
        public Input<int>? Mtu { get; set; }

        /// <summary>
        /// Subnet name. @EXAMPLE "10.228.247.0 BO1"
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Subnet network. @EXAMPLE "10.228.247.0"
        /// </summary>
        [Input("network", required: true)]
        public Input<string> Network { get; set; } = null!;

        /// <summary>
        /// The Subnets CIDR in the format 169.254.0.0/16
        /// </summary>
        [Input("networkAddress")]
        public Input<string>? NetworkAddress { get; set; }

        /// <summary>
        /// Type or protocol, IPv4 or IPv6, defaults to IPv4.
        /// </summary>
        [Input("networkType")]
        public Input<string>? NetworkType { get; set; }

        /// <summary>
        /// Template HTTP(S) Proxy ID to use within this subnet
        /// </summary>
        [Input("templateId")]
        public Input<int>? TemplateId { get; set; }

        /// <summary>
        /// TFTP Proxy ID to use within this subnet
        /// </summary>
        [Input("tftpId")]
        public Input<int>? TftpId { get; set; }

        /// <summary>
        /// Ending IP address for IP auto suggestion.
        /// </summary>
        [Input("to")]
        public Input<string>? To { get; set; }

        /// <summary>
        /// VLAN id that is in use in the subnet
        /// </summary>
        [Input("vlanid")]
        public Input<int>? Vlanid { get; set; }

        public SubnetArgs()
        {
        }
        public static new SubnetArgs Empty => new SubnetArgs();
    }

    public sealed class SubnetState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// @SUMMARY Foreman representation of a subnetwork.
        /// </summary>
        [Input("__meta_")]
        public Input<bool>? __meta_ { get; set; }

        /// <summary>
        /// BMC Proxy ID to use within this subnet
        /// </summary>
        [Input("bmcId")]
        public Input<int>? BmcId { get; set; }

        /// <summary>
        /// Default boot mode for instances assigned to this subnet. Values include: `"Static"`, `"DHCP"`.
        /// </summary>
        [Input("bootMode")]
        public Input<string>? BootMode { get; set; }

        /// <summary>
        /// Description of the subnet
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// DHCP Proxy ID to use within this subnet
        /// </summary>
        [Input("dhcpId")]
        public Input<int>? DhcpId { get; set; }

        /// <summary>
        /// Primary DNS server for this subnet.
        /// </summary>
        [Input("dnsPrimary")]
        public Input<string>? DnsPrimary { get; set; }

        /// <summary>
        /// Secondary DNS sever for this subnet.
        /// </summary>
        [Input("dnsSecondary")]
        public Input<string>? DnsSecondary { get; set; }

        [Input("domainIds")]
        private InputList<int>? _domainIds;

        /// <summary>
        /// Domains in which this subnet is part
        /// </summary>
        public InputList<int> DomainIds
        {
            get => _domainIds ?? (_domainIds = new InputList<int>());
            set => _domainIds = value;
        }

        /// <summary>
        /// Start IP address for IP auto suggestion.
        /// </summary>
        [Input("from")]
        public Input<string>? From { get; set; }

        /// <summary>
        /// Gateway server to use when connecting/communicating to anything not on the same network.
        /// </summary>
        [Input("gateway")]
        public Input<string>? Gateway { get; set; }

        /// <summary>
        /// HTTPBoot Proxy ID to use within this subnet
        /// </summary>
        [Input("httpbootId")]
        public Input<int>? HttpbootId { get; set; }

        /// <summary>
        /// IP address auto-suggestion for this subnet. Valid values include: `"DHCP"`, `"Internal DB"`, `"Random DB"`,`"None"`.
        /// </summary>
        [Input("ipam")]
        public Input<string>? Ipam { get; set; }

        /// <summary>
        /// Netmask for this subnet. @EXAMPLE "255.255.255.0"
        /// </summary>
        [Input("mask")]
        public Input<string>? Mask { get; set; }

        /// <summary>
        /// MTU value for the subnet
        /// </summary>
        [Input("mtu")]
        public Input<int>? Mtu { get; set; }

        /// <summary>
        /// Subnet name. @EXAMPLE "10.228.247.0 BO1"
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Subnet network. @EXAMPLE "10.228.247.0"
        /// </summary>
        [Input("network")]
        public Input<string>? Network { get; set; }

        /// <summary>
        /// The Subnets CIDR in the format 169.254.0.0/16
        /// </summary>
        [Input("networkAddress")]
        public Input<string>? NetworkAddress { get; set; }

        /// <summary>
        /// Type or protocol, IPv4 or IPv6, defaults to IPv4.
        /// </summary>
        [Input("networkType")]
        public Input<string>? NetworkType { get; set; }

        /// <summary>
        /// Template HTTP(S) Proxy ID to use within this subnet
        /// </summary>
        [Input("templateId")]
        public Input<int>? TemplateId { get; set; }

        /// <summary>
        /// TFTP Proxy ID to use within this subnet
        /// </summary>
        [Input("tftpId")]
        public Input<int>? TftpId { get; set; }

        /// <summary>
        /// Ending IP address for IP auto suggestion.
        /// </summary>
        [Input("to")]
        public Input<string>? To { get; set; }

        /// <summary>
        /// VLAN id that is in use in the subnet
        /// </summary>
        [Input("vlanid")]
        public Input<int>? Vlanid { get; set; }

        public SubnetState()
        {
        }
        public static new SubnetState Empty => new SubnetState();
    }
}
