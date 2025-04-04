// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetUser
    {
        public static Task<GetUserResult> InvokeAsync(GetUserArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserResult>("foreman:index/getUser:getUser", args ?? new GetUserArgs(), options.WithDefaults());

        public static Output<GetUserResult> Invoke(GetUserInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserResult>("foreman:index/getUser:getUser", args ?? new GetUserInvokeArgs(), options.WithDefaults());

        public static Output<GetUserResult> Invoke(GetUserInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserResult>("foreman:index/getUser:getUser", args ?? new GetUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserArgs : global::Pulumi.InvokeArgs
    {
        [Input("description")]
        public string? Description { get; set; }

        [Input("firstname")]
        public string? Firstname { get; set; }

        [Input("lastname")]
        public string? Lastname { get; set; }

        [Input("login")]
        public string? Login { get; set; }

        [Input("mail")]
        public string? Mail { get; set; }

        public GetUserArgs()
        {
        }
        public static new GetUserArgs Empty => new GetUserArgs();
    }

    public sealed class GetUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("firstname")]
        public Input<string>? Firstname { get; set; }

        [Input("lastname")]
        public Input<string>? Lastname { get; set; }

        [Input("login")]
        public Input<string>? Login { get; set; }

        [Input("mail")]
        public Input<string>? Mail { get; set; }

        public GetUserInvokeArgs()
        {
        }
        public static new GetUserInvokeArgs Empty => new GetUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserResult
    {
        public readonly bool Admin;
        public readonly int AuthSourceId;
        public readonly int DefaultLocationId;
        public readonly int DefaultOrganizationId;
        public readonly string? Description;
        public readonly string? Firstname;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? Lastname;
        public readonly string Locale;
        public readonly ImmutableArray<int> LocationIds;
        public readonly string? Login;
        public readonly string? Mail;
        public readonly ImmutableArray<int> OrganizationIds;
        public readonly string Password;

        [OutputConstructor]
        private GetUserResult(
            bool admin,

            int authSourceId,

            int defaultLocationId,

            int defaultOrganizationId,

            string? description,

            string? firstname,

            string id,

            string? lastname,

            string locale,

            ImmutableArray<int> locationIds,

            string? login,

            string? mail,

            ImmutableArray<int> organizationIds,

            string password)
        {
            Admin = admin;
            AuthSourceId = authSourceId;
            DefaultLocationId = defaultLocationId;
            DefaultOrganizationId = defaultOrganizationId;
            Description = description;
            Firstname = firstname;
            Id = id;
            Lastname = lastname;
            Locale = locale;
            LocationIds = locationIds;
            Login = login;
            Mail = mail;
            OrganizationIds = organizationIds;
            Password = password;
        }
    }
}
