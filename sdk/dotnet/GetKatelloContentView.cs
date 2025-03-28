// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetKatelloContentView
    {
        public static Task<GetKatelloContentViewResult> InvokeAsync(GetKatelloContentViewArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetKatelloContentViewResult>("foreman:index/getKatelloContentView:getKatelloContentView", args ?? new GetKatelloContentViewArgs(), options.WithDefaults());

        public static Output<GetKatelloContentViewResult> Invoke(GetKatelloContentViewInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetKatelloContentViewResult>("foreman:index/getKatelloContentView:getKatelloContentView", args ?? new GetKatelloContentViewInvokeArgs(), options.WithDefaults());

        public static Output<GetKatelloContentViewResult> Invoke(GetKatelloContentViewInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetKatelloContentViewResult>("foreman:index/getKatelloContentView:getKatelloContentView", args ?? new GetKatelloContentViewInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetKatelloContentViewArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetKatelloContentViewArgs()
        {
        }
        public static new GetKatelloContentViewArgs Empty => new GetKatelloContentViewArgs();
    }

    public sealed class GetKatelloContentViewInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetKatelloContentViewInvokeArgs()
        {
        }
        public static new GetKatelloContentViewInvokeArgs Empty => new GetKatelloContentViewInvokeArgs();
    }


    [OutputType]
    public sealed class GetKatelloContentViewResult
    {
        public readonly bool AutoPublish;
        public readonly ImmutableArray<int> ComponentIds;
        public readonly bool Composite;
        public readonly string Description;
        public readonly bool Filtered;
        public readonly ImmutableArray<Outputs.GetKatelloContentViewFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Label;
        public readonly int LatestVersionId;
        public readonly string Name;
        public readonly int OrganizationId;
        public readonly ImmutableArray<int> RepositoryIds;
        public readonly bool SolveDependencies;

        [OutputConstructor]
        private GetKatelloContentViewResult(
            bool autoPublish,

            ImmutableArray<int> componentIds,

            bool composite,

            string description,

            bool filtered,

            ImmutableArray<Outputs.GetKatelloContentViewFilterResult> filters,

            string id,

            string label,

            int latestVersionId,

            string name,

            int organizationId,

            ImmutableArray<int> repositoryIds,

            bool solveDependencies)
        {
            AutoPublish = autoPublish;
            ComponentIds = componentIds;
            Composite = composite;
            Description = description;
            Filtered = filtered;
            Filters = filters;
            Id = id;
            Label = label;
            LatestVersionId = latestVersionId;
            Name = name;
            OrganizationId = organizationId;
            RepositoryIds = repositoryIds;
            SolveDependencies = solveDependencies;
        }
    }
}
