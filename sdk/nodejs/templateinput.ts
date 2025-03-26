// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Templateinput extends pulumi.CustomResource {
    /**
     * Get an existing Templateinput resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TemplateinputState, opts?: pulumi.CustomResourceOptions): Templateinput {
        return new Templateinput(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/templateinput:Templateinput';

    /**
     * Returns true if the given object is an instance of Templateinput.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Templateinput {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Templateinput.__pulumiType;
    }

    /**
     * @SUMMARY Foreman representation of a template input.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    public readonly advanced!: pulumi.Output<boolean | undefined>;
    public readonly default!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly factName!: pulumi.Output<string | undefined>;
    public readonly hiddenValue!: pulumi.Output<boolean | undefined>;
    public readonly inputType!: pulumi.Output<string | undefined>;
    /**
     * The name of the template input
     */
    public readonly name!: pulumi.Output<string>;
    public readonly puppetClassName!: pulumi.Output<string | undefined>;
    public readonly puppetParameterName!: pulumi.Output<string | undefined>;
    public readonly required!: pulumi.Output<boolean | undefined>;
    public readonly resourceType!: pulumi.Output<string | undefined>;
    public /*out*/ readonly templateId!: pulumi.Output<number>;
    public readonly valueType!: pulumi.Output<string | undefined>;
    public readonly variableName!: pulumi.Output<string | undefined>;

    /**
     * Create a Templateinput resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TemplateinputArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TemplateinputArgs | TemplateinputState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TemplateinputState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["advanced"] = state ? state.advanced : undefined;
            resourceInputs["default"] = state ? state.default : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["factName"] = state ? state.factName : undefined;
            resourceInputs["hiddenValue"] = state ? state.hiddenValue : undefined;
            resourceInputs["inputType"] = state ? state.inputType : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["puppetClassName"] = state ? state.puppetClassName : undefined;
            resourceInputs["puppetParameterName"] = state ? state.puppetParameterName : undefined;
            resourceInputs["required"] = state ? state.required : undefined;
            resourceInputs["resourceType"] = state ? state.resourceType : undefined;
            resourceInputs["templateId"] = state ? state.templateId : undefined;
            resourceInputs["valueType"] = state ? state.valueType : undefined;
            resourceInputs["variableName"] = state ? state.variableName : undefined;
        } else {
            const args = argsOrState as TemplateinputArgs | undefined;
            if ((!args || args.default === undefined) && !opts.urn) {
                throw new Error("Missing required property 'default'");
            }
            resourceInputs["advanced"] = args ? args.advanced : undefined;
            resourceInputs["default"] = args ? args.default : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["factName"] = args ? args.factName : undefined;
            resourceInputs["hiddenValue"] = args ? args.hiddenValue : undefined;
            resourceInputs["inputType"] = args ? args.inputType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["puppetClassName"] = args ? args.puppetClassName : undefined;
            resourceInputs["puppetParameterName"] = args ? args.puppetParameterName : undefined;
            resourceInputs["required"] = args ? args.required : undefined;
            resourceInputs["resourceType"] = args ? args.resourceType : undefined;
            resourceInputs["valueType"] = args ? args.valueType : undefined;
            resourceInputs["variableName"] = args ? args.variableName : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
            resourceInputs["templateId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Templateinput.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Templateinput resources.
 */
export interface TemplateinputState {
    /**
     * @SUMMARY Foreman representation of a template input.
     */
    __meta_?: pulumi.Input<boolean>;
    advanced?: pulumi.Input<boolean>;
    default?: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    factName?: pulumi.Input<string>;
    hiddenValue?: pulumi.Input<boolean>;
    inputType?: pulumi.Input<string>;
    /**
     * The name of the template input
     */
    name?: pulumi.Input<string>;
    puppetClassName?: pulumi.Input<string>;
    puppetParameterName?: pulumi.Input<string>;
    required?: pulumi.Input<boolean>;
    resourceType?: pulumi.Input<string>;
    templateId?: pulumi.Input<number>;
    valueType?: pulumi.Input<string>;
    variableName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Templateinput resource.
 */
export interface TemplateinputArgs {
    advanced?: pulumi.Input<boolean>;
    default: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    factName?: pulumi.Input<string>;
    hiddenValue?: pulumi.Input<boolean>;
    inputType?: pulumi.Input<string>;
    /**
     * The name of the template input
     */
    name?: pulumi.Input<string>;
    puppetClassName?: pulumi.Input<string>;
    puppetParameterName?: pulumi.Input<string>;
    required?: pulumi.Input<boolean>;
    resourceType?: pulumi.Input<string>;
    valueType?: pulumi.Input<string>;
    variableName?: pulumi.Input<string>;
}
