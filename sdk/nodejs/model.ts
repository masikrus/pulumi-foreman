// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Model extends pulumi.CustomResource {
    /**
     * Get an existing Model resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ModelState, opts?: pulumi.CustomResourceOptions): Model {
        return new Model(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/model:Model';

    /**
     * Returns true if the given object is an instance of Model.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Model {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Model.__pulumiType;
    }

    /**
     * @SUMMARY Vendor-specific hardware model.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * Name of the specific hardware model.
     */
    public readonly hardwareModel!: pulumi.Output<string | undefined>;
    /**
     * Additional information about this hardware model.
     */
    public readonly info!: pulumi.Output<string | undefined>;
    /**
     * The name of the hardware model. @EXAMPLE "PowerEdge FC630"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Name or class of the hardware vendor.
     */
    public readonly vendorClass!: pulumi.Output<string | undefined>;

    /**
     * Create a Model resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ModelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ModelArgs | ModelState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ModelState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["hardwareModel"] = state ? state.hardwareModel : undefined;
            resourceInputs["info"] = state ? state.info : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["vendorClass"] = state ? state.vendorClass : undefined;
        } else {
            const args = argsOrState as ModelArgs | undefined;
            resourceInputs["hardwareModel"] = args ? args.hardwareModel : undefined;
            resourceInputs["info"] = args ? args.info : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["vendorClass"] = args ? args.vendorClass : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Model.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Model resources.
 */
export interface ModelState {
    /**
     * @SUMMARY Vendor-specific hardware model.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * Name of the specific hardware model.
     */
    hardwareModel?: pulumi.Input<string>;
    /**
     * Additional information about this hardware model.
     */
    info?: pulumi.Input<string>;
    /**
     * The name of the hardware model. @EXAMPLE "PowerEdge FC630"
     */
    name?: pulumi.Input<string>;
    /**
     * Name or class of the hardware vendor.
     */
    vendorClass?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Model resource.
 */
export interface ModelArgs {
    /**
     * Name of the specific hardware model.
     */
    hardwareModel?: pulumi.Input<string>;
    /**
     * Additional information about this hardware model.
     */
    info?: pulumi.Input<string>;
    /**
     * The name of the hardware model. @EXAMPLE "PowerEdge FC630"
     */
    name?: pulumi.Input<string>;
    /**
     * Name or class of the hardware vendor.
     */
    vendorClass?: pulumi.Input<string>;
}
