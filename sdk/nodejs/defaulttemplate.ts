// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Defaulttemplate extends pulumi.CustomResource {
    /**
     * Get an existing Defaulttemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaulttemplateState, opts?: pulumi.CustomResourceOptions): Defaulttemplate {
        return new Defaulttemplate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/defaulttemplate:Defaulttemplate';

    /**
     * Returns true if the given object is an instance of Defaulttemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Defaulttemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Defaulttemplate.__pulumiType;
    }

    /**
     * @SUMMARY Foreman representation of default Template. Default Templates serve as an identification string that defines
     * autonomy, authority, or control for a portion of a network.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * ID of the operating system to assign this Default Template to
     */
    public readonly operatingsystemId!: pulumi.Output<number | undefined>;
    /**
     * Id of the Provisioning Template
     */
    public readonly provisioningtemplateId!: pulumi.Output<number | undefined>;
    /**
     * Template Kind Id to define the Default Template
     */
    public readonly templatekindId!: pulumi.Output<number | undefined>;

    /**
     * Create a Defaulttemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DefaulttemplateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DefaulttemplateArgs | DefaulttemplateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DefaulttemplateState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["operatingsystemId"] = state ? state.operatingsystemId : undefined;
            resourceInputs["provisioningtemplateId"] = state ? state.provisioningtemplateId : undefined;
            resourceInputs["templatekindId"] = state ? state.templatekindId : undefined;
        } else {
            const args = argsOrState as DefaulttemplateArgs | undefined;
            resourceInputs["operatingsystemId"] = args ? args.operatingsystemId : undefined;
            resourceInputs["provisioningtemplateId"] = args ? args.provisioningtemplateId : undefined;
            resourceInputs["templatekindId"] = args ? args.templatekindId : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Defaulttemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Defaulttemplate resources.
 */
export interface DefaulttemplateState {
    /**
     * @SUMMARY Foreman representation of default Template. Default Templates serve as an identification string that defines
     * autonomy, authority, or control for a portion of a network.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * ID of the operating system to assign this Default Template to
     */
    operatingsystemId?: pulumi.Input<number>;
    /**
     * Id of the Provisioning Template
     */
    provisioningtemplateId?: pulumi.Input<number>;
    /**
     * Template Kind Id to define the Default Template
     */
    templatekindId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Defaulttemplate resource.
 */
export interface DefaulttemplateArgs {
    /**
     * ID of the operating system to assign this Default Template to
     */
    operatingsystemId?: pulumi.Input<number>;
    /**
     * Id of the Provisioning Template
     */
    provisioningtemplateId?: pulumi.Input<number>;
    /**
     * Template Kind Id to define the Default Template
     */
    templatekindId?: pulumi.Input<number>;
}
