// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Domain extends pulumi.CustomResource {
    /**
     * Get an existing Domain resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainState, opts?: pulumi.CustomResourceOptions): Domain {
        return new Domain(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/domain:Domain';

    /**
     * Returns true if the given object is an instance of Domain.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Domain {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Domain.__pulumiType;
    }

    /**
     * @SUMMARY Foreman representation of domain. Domains serve as an identification string that defines autonomy, authority,
     * or control for a portion of a network.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * Description of the domain
     */
    public readonly fullname!: pulumi.Output<string | undefined>;
    /**
     * The name of the domain - the full DNS domain name. @EXAMPLE "dev.dc1.company.com"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A map of parameters that will be saved as domain parameters in the domain config.
     */
    public readonly parameters!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Domain resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DomainArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DomainArgs | DomainState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DomainState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["fullname"] = state ? state.fullname : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["parameters"] = state ? state.parameters : undefined;
        } else {
            const args = argsOrState as DomainArgs | undefined;
            resourceInputs["fullname"] = args ? args.fullname : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Domain.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Domain resources.
 */
export interface DomainState {
    /**
     * @SUMMARY Foreman representation of domain. Domains serve as an identification string that defines autonomy, authority,
     * or control for a portion of a network.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * Description of the domain
     */
    fullname?: pulumi.Input<string>;
    /**
     * The name of the domain - the full DNS domain name. @EXAMPLE "dev.dc1.company.com"
     */
    name?: pulumi.Input<string>;
    /**
     * A map of parameters that will be saved as domain parameters in the domain config.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Domain resource.
 */
export interface DomainArgs {
    /**
     * Description of the domain
     */
    fullname?: pulumi.Input<string>;
    /**
     * The name of the domain - the full DNS domain name. @EXAMPLE "dev.dc1.company.com"
     */
    name?: pulumi.Input<string>;
    /**
     * A map of parameters that will be saved as domain parameters in the domain config.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
