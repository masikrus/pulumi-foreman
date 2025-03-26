// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetOperatingsystem
    {
        public static Task<GetOperatingsystemResult> InvokeAsync(GetOperatingsystemArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOperatingsystemResult>("foreman:index/getOperatingsystem:getOperatingsystem", args ?? new GetOperatingsystemArgs(), options.WithDefaults());

        public static Output<GetOperatingsystemResult> Invoke(GetOperatingsystemInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOperatingsystemResult>("foreman:index/getOperatingsystem:getOperatingsystem", args ?? new GetOperatingsystemInvokeArgs(), options.WithDefaults());

        public static Output<GetOperatingsystemResult> Invoke(GetOperatingsystemInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetOperatingsystemResult>("foreman:index/getOperatingsystem:getOperatingsystem", args ?? new GetOperatingsystemInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOperatingsystemArgs : global::Pulumi.InvokeArgs
    {
        [Input("title", required: true)]
        public string Title { get; set; } = null!;

        public GetOperatingsystemArgs()
        {
        }
        public static new GetOperatingsystemArgs Empty => new GetOperatingsystemArgs();
    }

    public sealed class GetOperatingsystemInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        public GetOperatingsystemInvokeArgs()
        {
        }
        public static new GetOperatingsystemInvokeArgs Empty => new GetOperatingsystemInvokeArgs();
    }


    [OutputType]
    public sealed class GetOperatingsystemResult
    {
        public readonly ImmutableArray<int> Architectures;
        public readonly string Description;
        public readonly string Family;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Major;
        public readonly ImmutableArray<int> Media;
        public readonly string Minor;
        public readonly string Name;
        public readonly ImmutableDictionary<string, string> Parameters;
        public readonly ImmutableArray<int> Partitiontables;
        public readonly string PasswordHash;
        public readonly ImmutableArray<int> ProvisioningTemplates;
        public readonly string ReleaseName;
        public readonly string Title;

        [OutputConstructor]
        private GetOperatingsystemResult(
            ImmutableArray<int> architectures,

            string description,

            string family,

            string id,

            string major,

            ImmutableArray<int> media,

            string minor,

            string name,

            ImmutableDictionary<string, string> parameters,

            ImmutableArray<int> partitiontables,

            string passwordHash,

            ImmutableArray<int> provisioningTemplates,

            string releaseName,

            string title)
        {
            Architectures = architectures;
            Description = description;
            Family = family;
            Id = id;
            Major = major;
            Media = media;
            Minor = minor;
            Name = name;
            Parameters = parameters;
            Partitiontables = partitiontables;
            PasswordHash = passwordHash;
            ProvisioningTemplates = provisioningTemplates;
            ReleaseName = releaseName;
            Title = title;
        }
    }
}
