// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetSmartclassparameter
    {
        public static Task<GetSmartclassparameterResult> InvokeAsync(GetSmartclassparameterArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSmartclassparameterResult>("foreman:index/getSmartclassparameter:getSmartclassparameter", args ?? new GetSmartclassparameterArgs(), options.WithDefaults());

        public static Output<GetSmartclassparameterResult> Invoke(GetSmartclassparameterInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSmartclassparameterResult>("foreman:index/getSmartclassparameter:getSmartclassparameter", args ?? new GetSmartclassparameterInvokeArgs(), options.WithDefaults());

        public static Output<GetSmartclassparameterResult> Invoke(GetSmartclassparameterInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetSmartclassparameterResult>("foreman:index/getSmartclassparameter:getSmartclassparameter", args ?? new GetSmartclassparameterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSmartclassparameterArgs : global::Pulumi.InvokeArgs
    {
        [Input("parameter", required: true)]
        public string Parameter { get; set; } = null!;

        [Input("puppetclassId", required: true)]
        public int PuppetclassId { get; set; }

        public GetSmartclassparameterArgs()
        {
        }
        public static new GetSmartclassparameterArgs Empty => new GetSmartclassparameterArgs();
    }

    public sealed class GetSmartclassparameterInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("parameter", required: true)]
        public Input<string> Parameter { get; set; } = null!;

        [Input("puppetclassId", required: true)]
        public Input<int> PuppetclassId { get; set; } = null!;

        public GetSmartclassparameterInvokeArgs()
        {
        }
        public static new GetSmartclassparameterInvokeArgs Empty => new GetSmartclassparameterInvokeArgs();
    }


    [OutputType]
    public sealed class GetSmartclassparameterResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Parameter;
        public readonly int PuppetclassId;

        [OutputConstructor]
        private GetSmartclassparameterResult(
            string id,

            string parameter,

            int puppetclassId)
        {
            Id = id;
            Parameter = parameter;
            PuppetclassId = puppetclassId;
        }
    }
}
