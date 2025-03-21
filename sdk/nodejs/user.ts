// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * @SUMMARY User can be used to allow access to foreman.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * If the user is allow admin privileges
     */
    public readonly admin!: pulumi.Output<boolean | undefined>;
    /**
     * Set the authentication source, i.e internal (1,default) or external (2)
     */
    public readonly authSourceId!: pulumi.Output<number | undefined>;
    /**
     * Default location for the user, if empty takes global default
     */
    public readonly defaultLocationId!: pulumi.Output<number | undefined>;
    /**
     * Default organization for the user, if empty takes global default
     */
    public readonly defaultOrganizationId!: pulumi.Output<number | undefined>;
    /**
     * Description of user
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * First name of the user
     */
    public readonly firstname!: pulumi.Output<string | undefined>;
    /**
     * Last name of user
     */
    public readonly lastname!: pulumi.Output<string | undefined>;
    /**
     * Sets the timezone/location of a user
     */
    public readonly locale!: pulumi.Output<string | undefined>;
    /**
     * List of all locations a user has access to
     */
    public readonly locationIds!: pulumi.Output<number[] | undefined>;
    /**
     * Username used for logging-in
     */
    public readonly login!: pulumi.Output<string>;
    /**
     * Email of user
     */
    public readonly mail!: pulumi.Output<string | undefined>;
    /**
     * List of all organizations a user has access to
     */
    public readonly organizationIds!: pulumi.Output<number[] | undefined>;
    /**
     * Password of user, required if authSourceId is 1 (internal)
     */
    public readonly password!: pulumi.Output<string | undefined>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["admin"] = state ? state.admin : undefined;
            resourceInputs["authSourceId"] = state ? state.authSourceId : undefined;
            resourceInputs["defaultLocationId"] = state ? state.defaultLocationId : undefined;
            resourceInputs["defaultOrganizationId"] = state ? state.defaultOrganizationId : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["firstname"] = state ? state.firstname : undefined;
            resourceInputs["lastname"] = state ? state.lastname : undefined;
            resourceInputs["locale"] = state ? state.locale : undefined;
            resourceInputs["locationIds"] = state ? state.locationIds : undefined;
            resourceInputs["login"] = state ? state.login : undefined;
            resourceInputs["mail"] = state ? state.mail : undefined;
            resourceInputs["organizationIds"] = state ? state.organizationIds : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if ((!args || args.login === undefined) && !opts.urn) {
                throw new Error("Missing required property 'login'");
            }
            resourceInputs["admin"] = args ? args.admin : undefined;
            resourceInputs["authSourceId"] = args ? args.authSourceId : undefined;
            resourceInputs["defaultLocationId"] = args ? args.defaultLocationId : undefined;
            resourceInputs["defaultOrganizationId"] = args ? args.defaultOrganizationId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["firstname"] = args ? args.firstname : undefined;
            resourceInputs["lastname"] = args ? args.lastname : undefined;
            resourceInputs["locale"] = args ? args.locale : undefined;
            resourceInputs["locationIds"] = args ? args.locationIds : undefined;
            resourceInputs["login"] = args ? args.login : undefined;
            resourceInputs["mail"] = args ? args.mail : undefined;
            resourceInputs["organizationIds"] = args ? args.organizationIds : undefined;
            resourceInputs["password"] = args?.password ? pulumi.secret(args.password) : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(User.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * @SUMMARY User can be used to allow access to foreman.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * If the user is allow admin privileges
     */
    admin?: pulumi.Input<boolean>;
    /**
     * Set the authentication source, i.e internal (1,default) or external (2)
     */
    authSourceId?: pulumi.Input<number>;
    /**
     * Default location for the user, if empty takes global default
     */
    defaultLocationId?: pulumi.Input<number>;
    /**
     * Default organization for the user, if empty takes global default
     */
    defaultOrganizationId?: pulumi.Input<number>;
    /**
     * Description of user
     */
    description?: pulumi.Input<string>;
    /**
     * First name of the user
     */
    firstname?: pulumi.Input<string>;
    /**
     * Last name of user
     */
    lastname?: pulumi.Input<string>;
    /**
     * Sets the timezone/location of a user
     */
    locale?: pulumi.Input<string>;
    /**
     * List of all locations a user has access to
     */
    locationIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Username used for logging-in
     */
    login?: pulumi.Input<string>;
    /**
     * Email of user
     */
    mail?: pulumi.Input<string>;
    /**
     * List of all organizations a user has access to
     */
    organizationIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Password of user, required if authSourceId is 1 (internal)
     */
    password?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * If the user is allow admin privileges
     */
    admin?: pulumi.Input<boolean>;
    /**
     * Set the authentication source, i.e internal (1,default) or external (2)
     */
    authSourceId?: pulumi.Input<number>;
    /**
     * Default location for the user, if empty takes global default
     */
    defaultLocationId?: pulumi.Input<number>;
    /**
     * Default organization for the user, if empty takes global default
     */
    defaultOrganizationId?: pulumi.Input<number>;
    /**
     * Description of user
     */
    description?: pulumi.Input<string>;
    /**
     * First name of the user
     */
    firstname?: pulumi.Input<string>;
    /**
     * Last name of user
     */
    lastname?: pulumi.Input<string>;
    /**
     * Sets the timezone/location of a user
     */
    locale?: pulumi.Input<string>;
    /**
     * List of all locations a user has access to
     */
    locationIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Username used for logging-in
     */
    login: pulumi.Input<string>;
    /**
     * Email of user
     */
    mail?: pulumi.Input<string>;
    /**
     * List of all organizations a user has access to
     */
    organizationIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Password of user, required if authSourceId is 1 (internal)
     */
    password?: pulumi.Input<string>;
}
