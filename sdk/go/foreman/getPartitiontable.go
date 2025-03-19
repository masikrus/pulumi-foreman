// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupPartitiontable(ctx *pulumi.Context, args *LookupPartitiontableArgs, opts ...pulumi.InvokeOption) (*LookupPartitiontableResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPartitiontableResult
	err := ctx.Invoke("foreman:index/getPartitiontable:getPartitiontable", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPartitiontable.
type LookupPartitiontableArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getPartitiontable.
type LookupPartitiontableResult struct {
	__meta_      bool   `pulumi:"__meta_"`
	AuditComment string `pulumi:"auditComment"`
	Description  string `pulumi:"description"`
	HostIds      []int  `pulumi:"hostIds"`
	HostgroupIds []int  `pulumi:"hostgroupIds"`
	// The provider-assigned unique ID for this managed resource.
	Id                 string `pulumi:"id"`
	Layout             string `pulumi:"layout"`
	Locked             bool   `pulumi:"locked"`
	Name               string `pulumi:"name"`
	OperatingsystemIds []int  `pulumi:"operatingsystemIds"`
	OsFamily           string `pulumi:"osFamily"`
	Snippet            bool   `pulumi:"snippet"`
}

func LookupPartitiontableOutput(ctx *pulumi.Context, args LookupPartitiontableOutputArgs, opts ...pulumi.InvokeOption) LookupPartitiontableResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupPartitiontableResultOutput, error) {
			args := v.(LookupPartitiontableArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getPartitiontable:getPartitiontable", args, LookupPartitiontableResultOutput{}, options).(LookupPartitiontableResultOutput), nil
		}).(LookupPartitiontableResultOutput)
}

// A collection of arguments for invoking getPartitiontable.
type LookupPartitiontableOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupPartitiontableOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPartitiontableArgs)(nil)).Elem()
}

// A collection of values returned by getPartitiontable.
type LookupPartitiontableResultOutput struct{ *pulumi.OutputState }

func (LookupPartitiontableResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPartitiontableResult)(nil)).Elem()
}

func (o LookupPartitiontableResultOutput) ToLookupPartitiontableResultOutput() LookupPartitiontableResultOutput {
	return o
}

func (o LookupPartitiontableResultOutput) ToLookupPartitiontableResultOutputWithContext(ctx context.Context) LookupPartitiontableResultOutput {
	return o
}

func (o LookupPartitiontableResultOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) bool { return v.__meta_ }).(pulumi.BoolOutput)
}

func (o LookupPartitiontableResultOutput) AuditComment() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) string { return v.AuditComment }).(pulumi.StringOutput)
}

func (o LookupPartitiontableResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupPartitiontableResultOutput) HostIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) []int { return v.HostIds }).(pulumi.IntArrayOutput)
}

func (o LookupPartitiontableResultOutput) HostgroupIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) []int { return v.HostgroupIds }).(pulumi.IntArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupPartitiontableResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupPartitiontableResultOutput) Layout() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) string { return v.Layout }).(pulumi.StringOutput)
}

func (o LookupPartitiontableResultOutput) Locked() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) bool { return v.Locked }).(pulumi.BoolOutput)
}

func (o LookupPartitiontableResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupPartitiontableResultOutput) OperatingsystemIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) []int { return v.OperatingsystemIds }).(pulumi.IntArrayOutput)
}

func (o LookupPartitiontableResultOutput) OsFamily() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) string { return v.OsFamily }).(pulumi.StringOutput)
}

func (o LookupPartitiontableResultOutput) Snippet() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupPartitiontableResult) bool { return v.Snippet }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPartitiontableResultOutput{})
}
