// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetParameter
    {
        public static Task<GetParameterResult> InvokeAsync(GetParameterArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetParameterResult>("foreman:index/getParameter:getParameter", args ?? new GetParameterArgs(), options.WithDefaults());

        public static Output<GetParameterResult> Invoke(GetParameterInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetParameterResult>("foreman:index/getParameter:getParameter", args ?? new GetParameterInvokeArgs(), options.WithDefaults());

        public static Output<GetParameterResult> Invoke(GetParameterInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetParameterResult>("foreman:index/getParameter:getParameter", args ?? new GetParameterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetParameterArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetParameterArgs()
        {
        }
        public static new GetParameterArgs Empty => new GetParameterArgs();
    }

    public sealed class GetParameterInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetParameterInvokeArgs()
        {
        }
        public static new GetParameterInvokeArgs Empty => new GetParameterInvokeArgs();
    }


    [OutputType]
    public sealed class GetParameterResult
    {
        public readonly int DomainId;
        public readonly int HostId;
        public readonly int HostgroupId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly int OperatingsystemId;
        public readonly int SubnetId;
        public readonly string Value;

        [OutputConstructor]
        private GetParameterResult(
            int domainId,

            int hostId,

            int hostgroupId,

            string id,

            string name,

            int operatingsystemId,

            int subnetId,

            string value)
        {
            DomainId = domainId;
            HostId = hostId;
            HostgroupId = hostgroupId;
            Id = id;
            Name = name;
            OperatingsystemId = operatingsystemId;
            SubnetId = subnetId;
            Value = value;
        }
    }
}
