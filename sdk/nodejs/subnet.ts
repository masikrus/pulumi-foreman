// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Subnet extends pulumi.CustomResource {
    /**
     * Get an existing Subnet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetState, opts?: pulumi.CustomResourceOptions): Subnet {
        return new Subnet(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/subnet:Subnet';

    /**
     * Returns true if the given object is an instance of Subnet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Subnet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Subnet.__pulumiType;
    }

    /**
     * @SUMMARY Foreman representation of a subnetwork.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * BMC Proxy ID to use within this subnet
     */
    public readonly bmcId!: pulumi.Output<number | undefined>;
    /**
     * Default boot mode for instances assigned to this subnet. Values include: `"Static"`, `"DHCP"`.
     */
    public readonly bootMode!: pulumi.Output<string | undefined>;
    /**
     * Description of the subnet
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * DHCP Proxy ID to use within this subnet
     */
    public readonly dhcpId!: pulumi.Output<number | undefined>;
    /**
     * Primary DNS server for this subnet.
     */
    public readonly dnsPrimary!: pulumi.Output<string | undefined>;
    /**
     * Secondary DNS sever for this subnet.
     */
    public readonly dnsSecondary!: pulumi.Output<string | undefined>;
    /**
     * Domains in which this subnet is part
     */
    public readonly domainIds!: pulumi.Output<number[] | undefined>;
    /**
     * Start IP address for IP auto suggestion.
     */
    public readonly from!: pulumi.Output<string | undefined>;
    /**
     * Gateway server to use when connecting/communicating to anything not on the same network.
     */
    public readonly gateway!: pulumi.Output<string | undefined>;
    /**
     * HTTPBoot Proxy ID to use within this subnet
     */
    public readonly httpbootId!: pulumi.Output<number | undefined>;
    /**
     * IP address auto-suggestion for this subnet. Valid values include: `"DHCP"`, `"Internal DB"`, `"Random DB"`,`"None"`.
     */
    public readonly ipam!: pulumi.Output<string | undefined>;
    /**
     * Netmask for this subnet. @EXAMPLE "255.255.255.0"
     */
    public readonly mask!: pulumi.Output<string>;
    /**
     * MTU value for the subnet
     */
    public readonly mtu!: pulumi.Output<number | undefined>;
    /**
     * Subnet name. @EXAMPLE "10.228.247.0 BO1"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Subnet network. @EXAMPLE "10.228.247.0"
     */
    public readonly network!: pulumi.Output<string>;
    /**
     * The Subnets CIDR in the format 169.254.0.0/16
     */
    public readonly networkAddress!: pulumi.Output<string | undefined>;
    /**
     * Type or protocol, IPv4 or IPv6, defaults to IPv4.
     */
    public readonly networkType!: pulumi.Output<string | undefined>;
    /**
     * Template HTTP(S) Proxy ID to use within this subnet
     */
    public readonly templateId!: pulumi.Output<number | undefined>;
    /**
     * TFTP Proxy ID to use within this subnet
     */
    public readonly tftpId!: pulumi.Output<number | undefined>;
    /**
     * Ending IP address for IP auto suggestion.
     */
    public readonly to!: pulumi.Output<string | undefined>;
    /**
     * VLAN id that is in use in the subnet
     */
    public readonly vlanid!: pulumi.Output<number | undefined>;

    /**
     * Create a Subnet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SubnetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SubnetArgs | SubnetState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SubnetState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["bmcId"] = state ? state.bmcId : undefined;
            resourceInputs["bootMode"] = state ? state.bootMode : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["dhcpId"] = state ? state.dhcpId : undefined;
            resourceInputs["dnsPrimary"] = state ? state.dnsPrimary : undefined;
            resourceInputs["dnsSecondary"] = state ? state.dnsSecondary : undefined;
            resourceInputs["domainIds"] = state ? state.domainIds : undefined;
            resourceInputs["from"] = state ? state.from : undefined;
            resourceInputs["gateway"] = state ? state.gateway : undefined;
            resourceInputs["httpbootId"] = state ? state.httpbootId : undefined;
            resourceInputs["ipam"] = state ? state.ipam : undefined;
            resourceInputs["mask"] = state ? state.mask : undefined;
            resourceInputs["mtu"] = state ? state.mtu : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["network"] = state ? state.network : undefined;
            resourceInputs["networkAddress"] = state ? state.networkAddress : undefined;
            resourceInputs["networkType"] = state ? state.networkType : undefined;
            resourceInputs["templateId"] = state ? state.templateId : undefined;
            resourceInputs["tftpId"] = state ? state.tftpId : undefined;
            resourceInputs["to"] = state ? state.to : undefined;
            resourceInputs["vlanid"] = state ? state.vlanid : undefined;
        } else {
            const args = argsOrState as SubnetArgs | undefined;
            if ((!args || args.mask === undefined) && !opts.urn) {
                throw new Error("Missing required property 'mask'");
            }
            if ((!args || args.network === undefined) && !opts.urn) {
                throw new Error("Missing required property 'network'");
            }
            resourceInputs["bmcId"] = args ? args.bmcId : undefined;
            resourceInputs["bootMode"] = args ? args.bootMode : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["dhcpId"] = args ? args.dhcpId : undefined;
            resourceInputs["dnsPrimary"] = args ? args.dnsPrimary : undefined;
            resourceInputs["dnsSecondary"] = args ? args.dnsSecondary : undefined;
            resourceInputs["domainIds"] = args ? args.domainIds : undefined;
            resourceInputs["from"] = args ? args.from : undefined;
            resourceInputs["gateway"] = args ? args.gateway : undefined;
            resourceInputs["httpbootId"] = args ? args.httpbootId : undefined;
            resourceInputs["ipam"] = args ? args.ipam : undefined;
            resourceInputs["mask"] = args ? args.mask : undefined;
            resourceInputs["mtu"] = args ? args.mtu : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["network"] = args ? args.network : undefined;
            resourceInputs["networkAddress"] = args ? args.networkAddress : undefined;
            resourceInputs["networkType"] = args ? args.networkType : undefined;
            resourceInputs["templateId"] = args ? args.templateId : undefined;
            resourceInputs["tftpId"] = args ? args.tftpId : undefined;
            resourceInputs["to"] = args ? args.to : undefined;
            resourceInputs["vlanid"] = args ? args.vlanid : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Subnet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Subnet resources.
 */
export interface SubnetState {
    /**
     * @SUMMARY Foreman representation of a subnetwork.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * BMC Proxy ID to use within this subnet
     */
    bmcId?: pulumi.Input<number>;
    /**
     * Default boot mode for instances assigned to this subnet. Values include: `"Static"`, `"DHCP"`.
     */
    bootMode?: pulumi.Input<string>;
    /**
     * Description of the subnet
     */
    description?: pulumi.Input<string>;
    /**
     * DHCP Proxy ID to use within this subnet
     */
    dhcpId?: pulumi.Input<number>;
    /**
     * Primary DNS server for this subnet.
     */
    dnsPrimary?: pulumi.Input<string>;
    /**
     * Secondary DNS sever for this subnet.
     */
    dnsSecondary?: pulumi.Input<string>;
    /**
     * Domains in which this subnet is part
     */
    domainIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Start IP address for IP auto suggestion.
     */
    from?: pulumi.Input<string>;
    /**
     * Gateway server to use when connecting/communicating to anything not on the same network.
     */
    gateway?: pulumi.Input<string>;
    /**
     * HTTPBoot Proxy ID to use within this subnet
     */
    httpbootId?: pulumi.Input<number>;
    /**
     * IP address auto-suggestion for this subnet. Valid values include: `"DHCP"`, `"Internal DB"`, `"Random DB"`,`"None"`.
     */
    ipam?: pulumi.Input<string>;
    /**
     * Netmask for this subnet. @EXAMPLE "255.255.255.0"
     */
    mask?: pulumi.Input<string>;
    /**
     * MTU value for the subnet
     */
    mtu?: pulumi.Input<number>;
    /**
     * Subnet name. @EXAMPLE "10.228.247.0 BO1"
     */
    name?: pulumi.Input<string>;
    /**
     * Subnet network. @EXAMPLE "10.228.247.0"
     */
    network?: pulumi.Input<string>;
    /**
     * The Subnets CIDR in the format 169.254.0.0/16
     */
    networkAddress?: pulumi.Input<string>;
    /**
     * Type or protocol, IPv4 or IPv6, defaults to IPv4.
     */
    networkType?: pulumi.Input<string>;
    /**
     * Template HTTP(S) Proxy ID to use within this subnet
     */
    templateId?: pulumi.Input<number>;
    /**
     * TFTP Proxy ID to use within this subnet
     */
    tftpId?: pulumi.Input<number>;
    /**
     * Ending IP address for IP auto suggestion.
     */
    to?: pulumi.Input<string>;
    /**
     * VLAN id that is in use in the subnet
     */
    vlanid?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Subnet resource.
 */
export interface SubnetArgs {
    /**
     * BMC Proxy ID to use within this subnet
     */
    bmcId?: pulumi.Input<number>;
    /**
     * Default boot mode for instances assigned to this subnet. Values include: `"Static"`, `"DHCP"`.
     */
    bootMode?: pulumi.Input<string>;
    /**
     * Description of the subnet
     */
    description?: pulumi.Input<string>;
    /**
     * DHCP Proxy ID to use within this subnet
     */
    dhcpId?: pulumi.Input<number>;
    /**
     * Primary DNS server for this subnet.
     */
    dnsPrimary?: pulumi.Input<string>;
    /**
     * Secondary DNS sever for this subnet.
     */
    dnsSecondary?: pulumi.Input<string>;
    /**
     * Domains in which this subnet is part
     */
    domainIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Start IP address for IP auto suggestion.
     */
    from?: pulumi.Input<string>;
    /**
     * Gateway server to use when connecting/communicating to anything not on the same network.
     */
    gateway?: pulumi.Input<string>;
    /**
     * HTTPBoot Proxy ID to use within this subnet
     */
    httpbootId?: pulumi.Input<number>;
    /**
     * IP address auto-suggestion for this subnet. Valid values include: `"DHCP"`, `"Internal DB"`, `"Random DB"`,`"None"`.
     */
    ipam?: pulumi.Input<string>;
    /**
     * Netmask for this subnet. @EXAMPLE "255.255.255.0"
     */
    mask: pulumi.Input<string>;
    /**
     * MTU value for the subnet
     */
    mtu?: pulumi.Input<number>;
    /**
     * Subnet name. @EXAMPLE "10.228.247.0 BO1"
     */
    name?: pulumi.Input<string>;
    /**
     * Subnet network. @EXAMPLE "10.228.247.0"
     */
    network: pulumi.Input<string>;
    /**
     * The Subnets CIDR in the format 169.254.0.0/16
     */
    networkAddress?: pulumi.Input<string>;
    /**
     * Type or protocol, IPv4 or IPv6, defaults to IPv4.
     */
    networkType?: pulumi.Input<string>;
    /**
     * Template HTTP(S) Proxy ID to use within this subnet
     */
    templateId?: pulumi.Input<number>;
    /**
     * TFTP Proxy ID to use within this subnet
     */
    tftpId?: pulumi.Input<number>;
    /**
     * Ending IP address for IP auto suggestion.
     */
    to?: pulumi.Input<string>;
    /**
     * VLAN id that is in use in the subnet
     */
    vlanid?: pulumi.Input<number>;
}
