// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetPartitiontable
    {
        public static Task<GetPartitiontableResult> InvokeAsync(GetPartitiontableArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPartitiontableResult>("foreman:index/getPartitiontable:getPartitiontable", args ?? new GetPartitiontableArgs(), options.WithDefaults());

        public static Output<GetPartitiontableResult> Invoke(GetPartitiontableInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPartitiontableResult>("foreman:index/getPartitiontable:getPartitiontable", args ?? new GetPartitiontableInvokeArgs(), options.WithDefaults());

        public static Output<GetPartitiontableResult> Invoke(GetPartitiontableInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPartitiontableResult>("foreman:index/getPartitiontable:getPartitiontable", args ?? new GetPartitiontableInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPartitiontableArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetPartitiontableArgs()
        {
        }
        public static new GetPartitiontableArgs Empty => new GetPartitiontableArgs();
    }

    public sealed class GetPartitiontableInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetPartitiontableInvokeArgs()
        {
        }
        public static new GetPartitiontableInvokeArgs Empty => new GetPartitiontableInvokeArgs();
    }


    [OutputType]
    public sealed class GetPartitiontableResult
    {
        public readonly string AuditComment;
        public readonly string Description;
        public readonly ImmutableArray<int> HostIds;
        public readonly ImmutableArray<int> HostgroupIds;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Layout;
        public readonly bool Locked;
        public readonly string Name;
        public readonly ImmutableArray<int> OperatingsystemIds;
        public readonly string OsFamily;
        public readonly bool Snippet;

        [OutputConstructor]
        private GetPartitiontableResult(
            string auditComment,

            string description,

            ImmutableArray<int> hostIds,

            ImmutableArray<int> hostgroupIds,

            string id,

            string layout,

            bool locked,

            string name,

            ImmutableArray<int> operatingsystemIds,

            string osFamily,

            bool snippet)
        {
            AuditComment = auditComment;
            Description = description;
            HostIds = hostIds;
            HostgroupIds = hostgroupIds;
            Id = id;
            Layout = layout;
            Locked = locked;
            Name = name;
            OperatingsystemIds = operatingsystemIds;
            OsFamily = osFamily;
            Snippet = snippet;
        }
    }
}
