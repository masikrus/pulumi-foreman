// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Jobtemplate extends pulumi.CustomResource {
    /**
     * Get an existing Jobtemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobtemplateState, opts?: pulumi.CustomResourceOptions): Jobtemplate {
        return new Jobtemplate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/jobtemplate:Jobtemplate';

    /**
     * Returns true if the given object is an instance of Jobtemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Jobtemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Jobtemplate.__pulumiType;
    }

    /**
     * @SUMMARY Foreman representation of a job template.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly descriptionFormat!: pulumi.Output<string | undefined>;
    public readonly jobCategory!: pulumi.Output<string>;
    public readonly locked!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the job template
     */
    public readonly name!: pulumi.Output<string>;
    public readonly providerType!: pulumi.Output<string | undefined>;
    public readonly snippet!: pulumi.Output<boolean | undefined>;
    /**
     * The template content itself
     */
    public readonly template!: pulumi.Output<string>;
    public readonly templateInputs!: pulumi.Output<outputs.JobtemplateTemplateInput[] | undefined>;

    /**
     * Create a Jobtemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: JobtemplateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: JobtemplateArgs | JobtemplateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as JobtemplateState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["descriptionFormat"] = state ? state.descriptionFormat : undefined;
            resourceInputs["jobCategory"] = state ? state.jobCategory : undefined;
            resourceInputs["locked"] = state ? state.locked : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["providerType"] = state ? state.providerType : undefined;
            resourceInputs["snippet"] = state ? state.snippet : undefined;
            resourceInputs["template"] = state ? state.template : undefined;
            resourceInputs["templateInputs"] = state ? state.templateInputs : undefined;
        } else {
            const args = argsOrState as JobtemplateArgs | undefined;
            if ((!args || args.jobCategory === undefined) && !opts.urn) {
                throw new Error("Missing required property 'jobCategory'");
            }
            if ((!args || args.template === undefined) && !opts.urn) {
                throw new Error("Missing required property 'template'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["descriptionFormat"] = args ? args.descriptionFormat : undefined;
            resourceInputs["jobCategory"] = args ? args.jobCategory : undefined;
            resourceInputs["locked"] = args ? args.locked : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["providerType"] = args ? args.providerType : undefined;
            resourceInputs["snippet"] = args ? args.snippet : undefined;
            resourceInputs["template"] = args ? args.template : undefined;
            resourceInputs["templateInputs"] = args ? args.templateInputs : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Jobtemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Jobtemplate resources.
 */
export interface JobtemplateState {
    /**
     * @SUMMARY Foreman representation of a job template.
     */
    __meta_?: pulumi.Input<boolean>;
    description?: pulumi.Input<string>;
    descriptionFormat?: pulumi.Input<string>;
    jobCategory?: pulumi.Input<string>;
    locked?: pulumi.Input<boolean>;
    /**
     * The name of the job template
     */
    name?: pulumi.Input<string>;
    providerType?: pulumi.Input<string>;
    snippet?: pulumi.Input<boolean>;
    /**
     * The template content itself
     */
    template?: pulumi.Input<string>;
    templateInputs?: pulumi.Input<pulumi.Input<inputs.JobtemplateTemplateInput>[]>;
}

/**
 * The set of arguments for constructing a Jobtemplate resource.
 */
export interface JobtemplateArgs {
    description?: pulumi.Input<string>;
    descriptionFormat?: pulumi.Input<string>;
    jobCategory: pulumi.Input<string>;
    locked?: pulumi.Input<boolean>;
    /**
     * The name of the job template
     */
    name?: pulumi.Input<string>;
    providerType?: pulumi.Input<string>;
    snippet?: pulumi.Input<boolean>;
    /**
     * The template content itself
     */
    template: pulumi.Input<string>;
    templateInputs?: pulumi.Input<pulumi.Input<inputs.JobtemplateTemplateInput>[]>;
}
