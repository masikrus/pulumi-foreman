// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Host extends pulumi.CustomResource {
    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostState, opts?: pulumi.CustomResourceOptions): Host {
        return new Host(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/host:Host';

    /**
     * Returns true if the given object is an instance of Host.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Host {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Host.__pulumiType;
    }

    /**
     * @SUMMARY A host managed by Foreman.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * ID of the architecture of this host
     */
    public readonly architectureId!: pulumi.Output<number>;
    /**
     * @deprecated The feature no longer exists
     */
    public readonly bmcSuccess!: pulumi.Output<boolean | undefined>;
    /**
     * Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
     */
    public readonly comment!: pulumi.Output<string>;
    /**
     * Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
     */
    public readonly computeAttributes!: pulumi.Output<string>;
    public readonly computeProfileId!: pulumi.Output<number>;
    public readonly computeResourceId!: pulumi.Output<number>;
    /**
     * IDs of the applied config groups.
     */
    public readonly configGroupIds!: pulumi.Output<number[]>;
    /**
     * ID of the domain to assign to the host.
     */
    public readonly domainId!: pulumi.Output<number>;
    /**
     * The domain name of the host.
     */
    public /*out*/ readonly domainName!: pulumi.Output<string>;
    /**
     * Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
     * boot to PXE and power on. Defaults to `false`.
     */
    public readonly enableBmc!: pulumi.Output<boolean | undefined>;
    /**
     * ID of the environment to assign to the host.
     */
    public readonly environmentId!: pulumi.Output<number>;
    /**
     * Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
     */
    public /*out*/ readonly fqdn!: pulumi.Output<string>;
    /**
     * ID of the hostgroup to assign to the host.
     */
    public readonly hostgroupId!: pulumi.Output<number>;
    /**
     * ID of an image to be used as base for this host when cloning
     */
    public readonly imageId!: pulumi.Output<number>;
    /**
     * Host interface information.
     */
    public readonly interfacesAttributes!: pulumi.Output<outputs.HostInterfacesAttribute[]>;
    /**
     * Manage power operations, e.g. power on, if host's build flag will be enabled.
     */
    public readonly managePowerOperations!: pulumi.Output<boolean | undefined>;
    /**
     * Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
     */
    public readonly managed!: pulumi.Output<boolean | undefined>;
    /**
     * ID of the medium mounted on the host.
     */
    public readonly mediumId!: pulumi.Output<number>;
    /**
     * ID of the hardware model if applicable
     */
    public readonly modelId!: pulumi.Output<number>;
    /**
     * Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
     * setting 'append_domain_name_for_hosts').
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * ID of the operating system to put on the host.
     */
    public readonly operatingsystemId!: pulumi.Output<number>;
    /**
     * ID of the user or usergroup that owns the host.
     */
    public readonly ownerId!: pulumi.Output<number>;
    /**
     * Owner of the host, must be either User ot Usergroup
     */
    public readonly ownerType!: pulumi.Output<string>;
    /**
     * A map of parameters that will be saved as host parameters in the machine config.
     */
    public readonly parameters!: pulumi.Output<{[key: string]: string}>;
    /**
     * Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
     */
    public readonly provisionMethod!: pulumi.Output<string | undefined>;
    /**
     * ID of the partition table the host should use
     */
    public readonly ptableId!: pulumi.Output<number>;
    /**
     * IDs of the applied puppet classes.
     */
    public readonly puppetClassIds!: pulumi.Output<number[]>;
    /**
     * Number of times to retry on a failed attempt to register or delete a host in foreman.
     */
    public readonly retryCount!: pulumi.Output<number | undefined>;
    /**
     * Default root password
     */
    public readonly rootPassword!: pulumi.Output<string | undefined>;
    /**
     * Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
     */
    public readonly setBuildFlag!: pulumi.Output<boolean | undefined>;
    /**
     * The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
     */
    public readonly shortname!: pulumi.Output<string>;
    /**
     * ID of the subnet the host should be placed in
     */
    public readonly subnetId!: pulumi.Output<number>;
    /**
     * Build token. Can be used to signal to Foreman that a host build is complete.
     */
    public /*out*/ readonly token!: pulumi.Output<string>;

    /**
     * Create a Host resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: HostArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: HostArgs | HostState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as HostState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["architectureId"] = state ? state.architectureId : undefined;
            resourceInputs["bmcSuccess"] = state ? state.bmcSuccess : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["computeAttributes"] = state ? state.computeAttributes : undefined;
            resourceInputs["computeProfileId"] = state ? state.computeProfileId : undefined;
            resourceInputs["computeResourceId"] = state ? state.computeResourceId : undefined;
            resourceInputs["configGroupIds"] = state ? state.configGroupIds : undefined;
            resourceInputs["domainId"] = state ? state.domainId : undefined;
            resourceInputs["domainName"] = state ? state.domainName : undefined;
            resourceInputs["enableBmc"] = state ? state.enableBmc : undefined;
            resourceInputs["environmentId"] = state ? state.environmentId : undefined;
            resourceInputs["fqdn"] = state ? state.fqdn : undefined;
            resourceInputs["hostgroupId"] = state ? state.hostgroupId : undefined;
            resourceInputs["imageId"] = state ? state.imageId : undefined;
            resourceInputs["interfacesAttributes"] = state ? state.interfacesAttributes : undefined;
            resourceInputs["managePowerOperations"] = state ? state.managePowerOperations : undefined;
            resourceInputs["managed"] = state ? state.managed : undefined;
            resourceInputs["mediumId"] = state ? state.mediumId : undefined;
            resourceInputs["modelId"] = state ? state.modelId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["operatingsystemId"] = state ? state.operatingsystemId : undefined;
            resourceInputs["ownerId"] = state ? state.ownerId : undefined;
            resourceInputs["ownerType"] = state ? state.ownerType : undefined;
            resourceInputs["parameters"] = state ? state.parameters : undefined;
            resourceInputs["provisionMethod"] = state ? state.provisionMethod : undefined;
            resourceInputs["ptableId"] = state ? state.ptableId : undefined;
            resourceInputs["puppetClassIds"] = state ? state.puppetClassIds : undefined;
            resourceInputs["retryCount"] = state ? state.retryCount : undefined;
            resourceInputs["rootPassword"] = state ? state.rootPassword : undefined;
            resourceInputs["setBuildFlag"] = state ? state.setBuildFlag : undefined;
            resourceInputs["shortname"] = state ? state.shortname : undefined;
            resourceInputs["subnetId"] = state ? state.subnetId : undefined;
            resourceInputs["token"] = state ? state.token : undefined;
        } else {
            const args = argsOrState as HostArgs | undefined;
            resourceInputs["architectureId"] = args ? args.architectureId : undefined;
            resourceInputs["bmcSuccess"] = args ? args.bmcSuccess : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["computeAttributes"] = args ? args.computeAttributes : undefined;
            resourceInputs["computeProfileId"] = args ? args.computeProfileId : undefined;
            resourceInputs["computeResourceId"] = args ? args.computeResourceId : undefined;
            resourceInputs["configGroupIds"] = args ? args.configGroupIds : undefined;
            resourceInputs["domainId"] = args ? args.domainId : undefined;
            resourceInputs["enableBmc"] = args ? args.enableBmc : undefined;
            resourceInputs["environmentId"] = args ? args.environmentId : undefined;
            resourceInputs["hostgroupId"] = args ? args.hostgroupId : undefined;
            resourceInputs["imageId"] = args ? args.imageId : undefined;
            resourceInputs["interfacesAttributes"] = args ? args.interfacesAttributes : undefined;
            resourceInputs["managePowerOperations"] = args ? args.managePowerOperations : undefined;
            resourceInputs["managed"] = args ? args.managed : undefined;
            resourceInputs["mediumId"] = args ? args.mediumId : undefined;
            resourceInputs["modelId"] = args ? args.modelId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["operatingsystemId"] = args ? args.operatingsystemId : undefined;
            resourceInputs["ownerId"] = args ? args.ownerId : undefined;
            resourceInputs["ownerType"] = args ? args.ownerType : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["provisionMethod"] = args ? args.provisionMethod : undefined;
            resourceInputs["ptableId"] = args ? args.ptableId : undefined;
            resourceInputs["puppetClassIds"] = args ? args.puppetClassIds : undefined;
            resourceInputs["retryCount"] = args ? args.retryCount : undefined;
            resourceInputs["rootPassword"] = args?.rootPassword ? pulumi.secret(args.rootPassword) : undefined;
            resourceInputs["setBuildFlag"] = args ? args.setBuildFlag : undefined;
            resourceInputs["shortname"] = args ? args.shortname : undefined;
            resourceInputs["subnetId"] = args ? args.subnetId : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["fqdn"] = undefined /*out*/;
            resourceInputs["token"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["rootPassword"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Host.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Host resources.
 */
export interface HostState {
    /**
     * @SUMMARY A host managed by Foreman.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * ID of the architecture of this host
     */
    architectureId?: pulumi.Input<number>;
    /**
     * @deprecated The feature no longer exists
     */
    bmcSuccess?: pulumi.Input<boolean>;
    /**
     * Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
     */
    comment?: pulumi.Input<string>;
    /**
     * Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
     */
    computeAttributes?: pulumi.Input<string>;
    computeProfileId?: pulumi.Input<number>;
    computeResourceId?: pulumi.Input<number>;
    /**
     * IDs of the applied config groups.
     */
    configGroupIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * ID of the domain to assign to the host.
     */
    domainId?: pulumi.Input<number>;
    /**
     * The domain name of the host.
     */
    domainName?: pulumi.Input<string>;
    /**
     * Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
     * boot to PXE and power on. Defaults to `false`.
     */
    enableBmc?: pulumi.Input<boolean>;
    /**
     * ID of the environment to assign to the host.
     */
    environmentId?: pulumi.Input<number>;
    /**
     * Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
     */
    fqdn?: pulumi.Input<string>;
    /**
     * ID of the hostgroup to assign to the host.
     */
    hostgroupId?: pulumi.Input<number>;
    /**
     * ID of an image to be used as base for this host when cloning
     */
    imageId?: pulumi.Input<number>;
    /**
     * Host interface information.
     */
    interfacesAttributes?: pulumi.Input<pulumi.Input<inputs.HostInterfacesAttribute>[]>;
    /**
     * Manage power operations, e.g. power on, if host's build flag will be enabled.
     */
    managePowerOperations?: pulumi.Input<boolean>;
    /**
     * Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
     */
    managed?: pulumi.Input<boolean>;
    /**
     * ID of the medium mounted on the host.
     */
    mediumId?: pulumi.Input<number>;
    /**
     * ID of the hardware model if applicable
     */
    modelId?: pulumi.Input<number>;
    /**
     * Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
     * setting 'append_domain_name_for_hosts').
     */
    name?: pulumi.Input<string>;
    /**
     * ID of the operating system to put on the host.
     */
    operatingsystemId?: pulumi.Input<number>;
    /**
     * ID of the user or usergroup that owns the host.
     */
    ownerId?: pulumi.Input<number>;
    /**
     * Owner of the host, must be either User ot Usergroup
     */
    ownerType?: pulumi.Input<string>;
    /**
     * A map of parameters that will be saved as host parameters in the machine config.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
     */
    provisionMethod?: pulumi.Input<string>;
    /**
     * ID of the partition table the host should use
     */
    ptableId?: pulumi.Input<number>;
    /**
     * IDs of the applied puppet classes.
     */
    puppetClassIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Number of times to retry on a failed attempt to register or delete a host in foreman.
     */
    retryCount?: pulumi.Input<number>;
    /**
     * Default root password
     */
    rootPassword?: pulumi.Input<string>;
    /**
     * Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
     */
    setBuildFlag?: pulumi.Input<boolean>;
    /**
     * The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
     */
    shortname?: pulumi.Input<string>;
    /**
     * ID of the subnet the host should be placed in
     */
    subnetId?: pulumi.Input<number>;
    /**
     * Build token. Can be used to signal to Foreman that a host build is complete.
     */
    token?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Host resource.
 */
export interface HostArgs {
    /**
     * ID of the architecture of this host
     */
    architectureId?: pulumi.Input<number>;
    /**
     * @deprecated The feature no longer exists
     */
    bmcSuccess?: pulumi.Input<boolean>;
    /**
     * Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
     */
    comment?: pulumi.Input<string>;
    /**
     * Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
     */
    computeAttributes?: pulumi.Input<string>;
    computeProfileId?: pulumi.Input<number>;
    computeResourceId?: pulumi.Input<number>;
    /**
     * IDs of the applied config groups.
     */
    configGroupIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * ID of the domain to assign to the host.
     */
    domainId?: pulumi.Input<number>;
    /**
     * Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
     * boot to PXE and power on. Defaults to `false`.
     */
    enableBmc?: pulumi.Input<boolean>;
    /**
     * ID of the environment to assign to the host.
     */
    environmentId?: pulumi.Input<number>;
    /**
     * ID of the hostgroup to assign to the host.
     */
    hostgroupId?: pulumi.Input<number>;
    /**
     * ID of an image to be used as base for this host when cloning
     */
    imageId?: pulumi.Input<number>;
    /**
     * Host interface information.
     */
    interfacesAttributes?: pulumi.Input<pulumi.Input<inputs.HostInterfacesAttribute>[]>;
    /**
     * Manage power operations, e.g. power on, if host's build flag will be enabled.
     */
    managePowerOperations?: pulumi.Input<boolean>;
    /**
     * Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
     */
    managed?: pulumi.Input<boolean>;
    /**
     * ID of the medium mounted on the host.
     */
    mediumId?: pulumi.Input<number>;
    /**
     * ID of the hardware model if applicable
     */
    modelId?: pulumi.Input<number>;
    /**
     * Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
     * setting 'append_domain_name_for_hosts').
     */
    name?: pulumi.Input<string>;
    /**
     * ID of the operating system to put on the host.
     */
    operatingsystemId?: pulumi.Input<number>;
    /**
     * ID of the user or usergroup that owns the host.
     */
    ownerId?: pulumi.Input<number>;
    /**
     * Owner of the host, must be either User ot Usergroup
     */
    ownerType?: pulumi.Input<string>;
    /**
     * A map of parameters that will be saved as host parameters in the machine config.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
     */
    provisionMethod?: pulumi.Input<string>;
    /**
     * ID of the partition table the host should use
     */
    ptableId?: pulumi.Input<number>;
    /**
     * IDs of the applied puppet classes.
     */
    puppetClassIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Number of times to retry on a failed attempt to register or delete a host in foreman.
     */
    retryCount?: pulumi.Input<number>;
    /**
     * Default root password
     */
    rootPassword?: pulumi.Input<string>;
    /**
     * Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
     */
    setBuildFlag?: pulumi.Input<boolean>;
    /**
     * The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
     */
    shortname?: pulumi.Input<string>;
    /**
     * ID of the subnet the host should be placed in
     */
    subnetId?: pulumi.Input<number>;
}
