// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetDomain
    {
        public static Task<GetDomainResult> InvokeAsync(GetDomainArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDomainResult>("foreman:index/getDomain:getDomain", args ?? new GetDomainArgs(), options.WithDefaults());

        public static Output<GetDomainResult> Invoke(GetDomainInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDomainResult>("foreman:index/getDomain:getDomain", args ?? new GetDomainInvokeArgs(), options.WithDefaults());

        public static Output<GetDomainResult> Invoke(GetDomainInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetDomainResult>("foreman:index/getDomain:getDomain", args ?? new GetDomainInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDomainArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetDomainArgs()
        {
        }
        public static new GetDomainArgs Empty => new GetDomainArgs();
    }

    public sealed class GetDomainInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetDomainInvokeArgs()
        {
        }
        public static new GetDomainInvokeArgs Empty => new GetDomainInvokeArgs();
    }


    [OutputType]
    public sealed class GetDomainResult
    {
        public readonly bool __meta_;
        public readonly string Fullname;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly ImmutableDictionary<string, string> Parameters;

        [OutputConstructor]
        private GetDomainResult(
            bool __meta_,

            string fullname,

            string id,

            string name,

            ImmutableDictionary<string, string> parameters)
        {
            this.__meta_ = __meta_;
            Fullname = fullname;
            Id = id;
            Name = name;
            Parameters = parameters;
        }
    }
}
