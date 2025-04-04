// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Provisioningtemplate extends pulumi.CustomResource {
    /**
     * Get an existing Provisioningtemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProvisioningtemplateState, opts?: pulumi.CustomResourceOptions): Provisioningtemplate {
        return new Provisioningtemplate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/provisioningtemplate:Provisioningtemplate';

    /**
     * Returns true if the given object is an instance of Provisioningtemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provisioningtemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Provisioningtemplate.__pulumiType;
    }

    /**
     * @SUMMARY Provisioning templates are scripts used to describe how to bootstrap and install the operating system on the
     * host.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * Notes and comments for auditing purposes.
     */
    public readonly auditComment!: pulumi.Output<string | undefined>;
    /**
     * A description of the provisioning template.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Whether or not the template is locked for editing.
     */
    public readonly locked!: pulumi.Output<boolean | undefined>;
    /**
     * Name of the provisioning template. @EXAMPLE "AutoYaST default"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * IDs of the operating systems associated with this provisioning template.
     */
    public readonly operatingsystemIds!: pulumi.Output<number[]>;
    /**
     * Whether or not the provisioning template is a snippet be used by other templates.
     */
    public readonly snippet!: pulumi.Output<boolean | undefined>;
    /**
     * The markup and code of the provisioning template. @EXAMPLE "void"
     */
    public readonly template!: pulumi.Output<string>;
    /**
     * How templates are determined: When editing a template, you must assign a list of operating systems which this template
     * can be used with. Optionally, you can restrict a template to a list of host groups and/or environments. When a host
     * requests a template, Foreman will select the best match from the available templates of that type in the following
     * order: 1. host group and environment 2. host group only 3. environment only 4. operating system default Template
     * combinations attributes contains an array of hostgroup IDs and environment ID combinations so they can be used in the
     * provisioning template selection described above.
     */
    public readonly templateCombinationsAttributes!: pulumi.Output<outputs.ProvisioningtemplateTemplateCombinationsAttribute[] | undefined>;
    /**
     * ID of the template kind which categorizes the provisioning template. Optional for snippets, otherwise required.
     */
    public readonly templateKindId!: pulumi.Output<number | undefined>;

    /**
     * Create a Provisioningtemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProvisioningtemplateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProvisioningtemplateArgs | ProvisioningtemplateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProvisioningtemplateState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["auditComment"] = state ? state.auditComment : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["locked"] = state ? state.locked : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["operatingsystemIds"] = state ? state.operatingsystemIds : undefined;
            resourceInputs["snippet"] = state ? state.snippet : undefined;
            resourceInputs["template"] = state ? state.template : undefined;
            resourceInputs["templateCombinationsAttributes"] = state ? state.templateCombinationsAttributes : undefined;
            resourceInputs["templateKindId"] = state ? state.templateKindId : undefined;
        } else {
            const args = argsOrState as ProvisioningtemplateArgs | undefined;
            if ((!args || args.template === undefined) && !opts.urn) {
                throw new Error("Missing required property 'template'");
            }
            resourceInputs["auditComment"] = args ? args.auditComment : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["locked"] = args ? args.locked : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["operatingsystemIds"] = args ? args.operatingsystemIds : undefined;
            resourceInputs["snippet"] = args ? args.snippet : undefined;
            resourceInputs["template"] = args ? args.template : undefined;
            resourceInputs["templateCombinationsAttributes"] = args ? args.templateCombinationsAttributes : undefined;
            resourceInputs["templateKindId"] = args ? args.templateKindId : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Provisioningtemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Provisioningtemplate resources.
 */
export interface ProvisioningtemplateState {
    /**
     * @SUMMARY Provisioning templates are scripts used to describe how to bootstrap and install the operating system on the
     * host.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * Notes and comments for auditing purposes.
     */
    auditComment?: pulumi.Input<string>;
    /**
     * A description of the provisioning template.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether or not the template is locked for editing.
     */
    locked?: pulumi.Input<boolean>;
    /**
     * Name of the provisioning template. @EXAMPLE "AutoYaST default"
     */
    name?: pulumi.Input<string>;
    /**
     * IDs of the operating systems associated with this provisioning template.
     */
    operatingsystemIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Whether or not the provisioning template is a snippet be used by other templates.
     */
    snippet?: pulumi.Input<boolean>;
    /**
     * The markup and code of the provisioning template. @EXAMPLE "void"
     */
    template?: pulumi.Input<string>;
    /**
     * How templates are determined: When editing a template, you must assign a list of operating systems which this template
     * can be used with. Optionally, you can restrict a template to a list of host groups and/or environments. When a host
     * requests a template, Foreman will select the best match from the available templates of that type in the following
     * order: 1. host group and environment 2. host group only 3. environment only 4. operating system default Template
     * combinations attributes contains an array of hostgroup IDs and environment ID combinations so they can be used in the
     * provisioning template selection described above.
     */
    templateCombinationsAttributes?: pulumi.Input<pulumi.Input<inputs.ProvisioningtemplateTemplateCombinationsAttribute>[]>;
    /**
     * ID of the template kind which categorizes the provisioning template. Optional for snippets, otherwise required.
     */
    templateKindId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Provisioningtemplate resource.
 */
export interface ProvisioningtemplateArgs {
    /**
     * Notes and comments for auditing purposes.
     */
    auditComment?: pulumi.Input<string>;
    /**
     * A description of the provisioning template.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether or not the template is locked for editing.
     */
    locked?: pulumi.Input<boolean>;
    /**
     * Name of the provisioning template. @EXAMPLE "AutoYaST default"
     */
    name?: pulumi.Input<string>;
    /**
     * IDs of the operating systems associated with this provisioning template.
     */
    operatingsystemIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Whether or not the provisioning template is a snippet be used by other templates.
     */
    snippet?: pulumi.Input<boolean>;
    /**
     * The markup and code of the provisioning template. @EXAMPLE "void"
     */
    template: pulumi.Input<string>;
    /**
     * How templates are determined: When editing a template, you must assign a list of operating systems which this template
     * can be used with. Optionally, you can restrict a template to a list of host groups and/or environments. When a host
     * requests a template, Foreman will select the best match from the available templates of that type in the following
     * order: 1. host group and environment 2. host group only 3. environment only 4. operating system default Template
     * combinations attributes contains an array of hostgroup IDs and environment ID combinations so they can be used in the
     * provisioning template selection described above.
     */
    templateCombinationsAttributes?: pulumi.Input<pulumi.Input<inputs.ProvisioningtemplateTemplateCombinationsAttribute>[]>;
    /**
     * ID of the template kind which categorizes the provisioning template. Optional for snippets, otherwise required.
     */
    templateKindId?: pulumi.Input<number>;
}
