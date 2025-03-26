// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupDomain(ctx *pulumi.Context, args *LookupDomainArgs, opts ...pulumi.InvokeOption) (*LookupDomainResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDomainResult
	err := ctx.Invoke("foreman:index/getDomain:getDomain", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDomain.
type LookupDomainArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getDomain.
type LookupDomainResult struct {
	Fullname string `pulumi:"fullname"`
	// The provider-assigned unique ID for this managed resource.
	Id         string            `pulumi:"id"`
	Name       string            `pulumi:"name"`
	Parameters map[string]string `pulumi:"parameters"`
}

func LookupDomainOutput(ctx *pulumi.Context, args LookupDomainOutputArgs, opts ...pulumi.InvokeOption) LookupDomainResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupDomainResultOutput, error) {
			args := v.(LookupDomainArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getDomain:getDomain", args, LookupDomainResultOutput{}, options).(LookupDomainResultOutput), nil
		}).(LookupDomainResultOutput)
}

// A collection of arguments for invoking getDomain.
type LookupDomainOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupDomainOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDomainArgs)(nil)).Elem()
}

// A collection of values returned by getDomain.
type LookupDomainResultOutput struct{ *pulumi.OutputState }

func (LookupDomainResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDomainResult)(nil)).Elem()
}

func (o LookupDomainResultOutput) ToLookupDomainResultOutput() LookupDomainResultOutput {
	return o
}

func (o LookupDomainResultOutput) ToLookupDomainResultOutputWithContext(ctx context.Context) LookupDomainResultOutput {
	return o
}

func (o LookupDomainResultOutput) Fullname() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDomainResult) string { return v.Fullname }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupDomainResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDomainResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupDomainResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDomainResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupDomainResultOutput) Parameters() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupDomainResult) map[string]string { return v.Parameters }).(pulumi.StringMapOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDomainResultOutput{})
}
