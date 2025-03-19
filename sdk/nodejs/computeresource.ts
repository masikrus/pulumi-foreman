// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Computeresource extends pulumi.CustomResource {
    /**
     * Get an existing Computeresource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeresourceState, opts?: pulumi.CustomResourceOptions): Computeresource {
        return new Computeresource(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/computeresource:Computeresource';

    /**
     * Returns true if the given object is an instance of Computeresource.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Computeresource {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Computeresource.__pulumiType;
    }

    /**
     * @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
     * autonomy, authority, or control for a portion of a network.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * For VMware only
     */
    public readonly cachingenabled!: pulumi.Output<boolean | undefined>;
    /**
     * For oVirt, VMware Datacenter
     */
    public readonly datacenter!: pulumi.Output<string | undefined>;
    /**
     * Description of the compute resource
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
     */
    public readonly displaytype!: pulumi.Output<string | undefined>;
    /**
     * The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
     * "Openstack", "Rackspace", "GCE"
     */
    public readonly hypervisor!: pulumi.Output<string>;
    /**
     * Name of the compute resource
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * For VMware
     */
    public readonly server!: pulumi.Output<string | undefined>;
    /**
     * For Libvirt and VMware only
     */
    public readonly setconsolepassword!: pulumi.Output<boolean | undefined>;
    /**
     * URL for Libvirt, oVirt, OpenStack and Rackspace
     */
    public readonly url!: pulumi.Output<string>;
    /**
     * Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
     */
    public readonly user!: pulumi.Output<string | undefined>;

    /**
     * Create a Computeresource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ComputeresourceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ComputeresourceArgs | ComputeresourceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ComputeresourceState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["cachingenabled"] = state ? state.cachingenabled : undefined;
            resourceInputs["datacenter"] = state ? state.datacenter : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["displaytype"] = state ? state.displaytype : undefined;
            resourceInputs["hypervisor"] = state ? state.hypervisor : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["server"] = state ? state.server : undefined;
            resourceInputs["setconsolepassword"] = state ? state.setconsolepassword : undefined;
            resourceInputs["url"] = state ? state.url : undefined;
            resourceInputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as ComputeresourceArgs | undefined;
            if ((!args || args.hypervisor === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hypervisor'");
            }
            if ((!args || args.url === undefined) && !opts.urn) {
                throw new Error("Missing required property 'url'");
            }
            resourceInputs["cachingenabled"] = args ? args.cachingenabled : undefined;
            resourceInputs["datacenter"] = args ? args.datacenter : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["displaytype"] = args ? args.displaytype : undefined;
            resourceInputs["hypervisor"] = args ? args.hypervisor : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["password"] = args?.password ? pulumi.secret(args.password) : undefined;
            resourceInputs["server"] = args ? args.server : undefined;
            resourceInputs["setconsolepassword"] = args ? args.setconsolepassword : undefined;
            resourceInputs["url"] = args ? args.url : undefined;
            resourceInputs["user"] = args ? args.user : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Computeresource.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Computeresource resources.
 */
export interface ComputeresourceState {
    /**
     * @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
     * autonomy, authority, or control for a portion of a network.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * For VMware only
     */
    cachingenabled?: pulumi.Input<boolean>;
    /**
     * For oVirt, VMware Datacenter
     */
    datacenter?: pulumi.Input<string>;
    /**
     * Description of the compute resource
     */
    description?: pulumi.Input<string>;
    /**
     * For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
     */
    displaytype?: pulumi.Input<string>;
    /**
     * The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
     * "Openstack", "Rackspace", "GCE"
     */
    hypervisor?: pulumi.Input<string>;
    /**
     * Name of the compute resource
     */
    name?: pulumi.Input<string>;
    /**
     * Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
     */
    password?: pulumi.Input<string>;
    /**
     * For VMware
     */
    server?: pulumi.Input<string>;
    /**
     * For Libvirt and VMware only
     */
    setconsolepassword?: pulumi.Input<boolean>;
    /**
     * URL for Libvirt, oVirt, OpenStack and Rackspace
     */
    url?: pulumi.Input<string>;
    /**
     * Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
     */
    user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Computeresource resource.
 */
export interface ComputeresourceArgs {
    /**
     * For VMware only
     */
    cachingenabled?: pulumi.Input<boolean>;
    /**
     * For oVirt, VMware Datacenter
     */
    datacenter?: pulumi.Input<string>;
    /**
     * Description of the compute resource
     */
    description?: pulumi.Input<string>;
    /**
     * For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
     */
    displaytype?: pulumi.Input<string>;
    /**
     * The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
     * "Openstack", "Rackspace", "GCE"
     */
    hypervisor: pulumi.Input<string>;
    /**
     * Name of the compute resource
     */
    name?: pulumi.Input<string>;
    /**
     * Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
     */
    password?: pulumi.Input<string>;
    /**
     * For VMware
     */
    server?: pulumi.Input<string>;
    /**
     * For Libvirt and VMware only
     */
    setconsolepassword?: pulumi.Input<boolean>;
    /**
     * URL for Libvirt, oVirt, OpenStack and Rackspace
     */
    url: pulumi.Input<string>;
    /**
     * Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
     */
    user?: pulumi.Input<string>;
}
