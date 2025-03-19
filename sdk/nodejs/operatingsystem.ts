// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Operatingsystem extends pulumi.CustomResource {
    /**
     * Get an existing Operatingsystem resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OperatingsystemState, opts?: pulumi.CustomResourceOptions): Operatingsystem {
        return new Operatingsystem(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/operatingsystem:Operatingsystem';

    /**
     * Returns true if the given object is an instance of Operatingsystem.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Operatingsystem {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Operatingsystem.__pulumiType;
    }

    /**
     * @SUMMARY Foreman representation of an operating system.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * Identifiers of attached architectures
     */
    public readonly architectures!: pulumi.Output<number[] | undefined>;
    /**
     * Additional operating system information.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
     * `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
     */
    public readonly family!: pulumi.Output<string | undefined>;
    /**
     * Major release version. @EXAMPLE "7"
     */
    public readonly major!: pulumi.Output<string>;
    /**
     * Identifiers of attached media
     */
    public readonly media!: pulumi.Output<number[] | undefined>;
    /**
     * Minor release version. @EXAMPLE "4"
     */
    public readonly minor!: pulumi.Output<string | undefined>;
    /**
     * Operating system name. @EXAMPLE "CentOS"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A map of parameters that will be saved as operating system parameters in the os config.
     */
    public readonly parameters!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Identifiers of attached partition tables
     */
    public readonly partitiontables!: pulumi.Output<number[]>;
    /**
     * Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
     */
    public readonly passwordHash!: pulumi.Output<string | undefined>;
    /**
     * Identifiers of attached provisioning templates
     */
    public readonly provisioningTemplates!: pulumi.Output<number[]>;
    /**
     * Code name or release name for the specific operating system version.
     */
    public readonly releaseName!: pulumi.Output<string | undefined>;
    /**
     * The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
     * system release.
     */
    public /*out*/ readonly title!: pulumi.Output<string>;

    /**
     * Create a Operatingsystem resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OperatingsystemArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OperatingsystemArgs | OperatingsystemState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OperatingsystemState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["architectures"] = state ? state.architectures : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["family"] = state ? state.family : undefined;
            resourceInputs["major"] = state ? state.major : undefined;
            resourceInputs["media"] = state ? state.media : undefined;
            resourceInputs["minor"] = state ? state.minor : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["parameters"] = state ? state.parameters : undefined;
            resourceInputs["partitiontables"] = state ? state.partitiontables : undefined;
            resourceInputs["passwordHash"] = state ? state.passwordHash : undefined;
            resourceInputs["provisioningTemplates"] = state ? state.provisioningTemplates : undefined;
            resourceInputs["releaseName"] = state ? state.releaseName : undefined;
            resourceInputs["title"] = state ? state.title : undefined;
        } else {
            const args = argsOrState as OperatingsystemArgs | undefined;
            if ((!args || args.major === undefined) && !opts.urn) {
                throw new Error("Missing required property 'major'");
            }
            resourceInputs["architectures"] = args ? args.architectures : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["family"] = args ? args.family : undefined;
            resourceInputs["major"] = args ? args.major : undefined;
            resourceInputs["media"] = args ? args.media : undefined;
            resourceInputs["minor"] = args ? args.minor : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["partitiontables"] = args ? args.partitiontables : undefined;
            resourceInputs["passwordHash"] = args ? args.passwordHash : undefined;
            resourceInputs["provisioningTemplates"] = args ? args.provisioningTemplates : undefined;
            resourceInputs["releaseName"] = args ? args.releaseName : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
            resourceInputs["title"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Operatingsystem.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Operatingsystem resources.
 */
export interface OperatingsystemState {
    /**
     * @SUMMARY Foreman representation of an operating system.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * Identifiers of attached architectures
     */
    architectures?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Additional operating system information.
     */
    description?: pulumi.Input<string>;
    /**
     * Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
     * `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
     */
    family?: pulumi.Input<string>;
    /**
     * Major release version. @EXAMPLE "7"
     */
    major?: pulumi.Input<string>;
    /**
     * Identifiers of attached media
     */
    media?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Minor release version. @EXAMPLE "4"
     */
    minor?: pulumi.Input<string>;
    /**
     * Operating system name. @EXAMPLE "CentOS"
     */
    name?: pulumi.Input<string>;
    /**
     * A map of parameters that will be saved as operating system parameters in the os config.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Identifiers of attached partition tables
     */
    partitiontables?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
     */
    passwordHash?: pulumi.Input<string>;
    /**
     * Identifiers of attached provisioning templates
     */
    provisioningTemplates?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Code name or release name for the specific operating system version.
     */
    releaseName?: pulumi.Input<string>;
    /**
     * The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
     * system release.
     */
    title?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Operatingsystem resource.
 */
export interface OperatingsystemArgs {
    /**
     * Identifiers of attached architectures
     */
    architectures?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Additional operating system information.
     */
    description?: pulumi.Input<string>;
    /**
     * Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
     * `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
     */
    family?: pulumi.Input<string>;
    /**
     * Major release version. @EXAMPLE "7"
     */
    major: pulumi.Input<string>;
    /**
     * Identifiers of attached media
     */
    media?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Minor release version. @EXAMPLE "4"
     */
    minor?: pulumi.Input<string>;
    /**
     * Operating system name. @EXAMPLE "CentOS"
     */
    name?: pulumi.Input<string>;
    /**
     * A map of parameters that will be saved as operating system parameters in the os config.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Identifiers of attached partition tables
     */
    partitiontables?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
     */
    passwordHash?: pulumi.Input<string>;
    /**
     * Identifiers of attached provisioning templates
     */
    provisioningTemplates?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Code name or release name for the specific operating system version.
     */
    releaseName?: pulumi.Input<string>;
}
