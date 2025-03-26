// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupKatelloSyncPlan(ctx *pulumi.Context, args *LookupKatelloSyncPlanArgs, opts ...pulumi.InvokeOption) (*LookupKatelloSyncPlanResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupKatelloSyncPlanResult
	err := ctx.Invoke("foreman:index/getKatelloSyncPlan:getKatelloSyncPlan", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKatelloSyncPlan.
type LookupKatelloSyncPlanArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getKatelloSyncPlan.
type LookupKatelloSyncPlanResult struct {
	CronExpression string `pulumi:"cronExpression"`
	Description    string `pulumi:"description"`
	Enabled        bool   `pulumi:"enabled"`
	// The provider-assigned unique ID for this managed resource.
	Id       string `pulumi:"id"`
	Interval string `pulumi:"interval"`
	Name     string `pulumi:"name"`
	SyncDate string `pulumi:"syncDate"`
}

func LookupKatelloSyncPlanOutput(ctx *pulumi.Context, args LookupKatelloSyncPlanOutputArgs, opts ...pulumi.InvokeOption) LookupKatelloSyncPlanResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupKatelloSyncPlanResultOutput, error) {
			args := v.(LookupKatelloSyncPlanArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getKatelloSyncPlan:getKatelloSyncPlan", args, LookupKatelloSyncPlanResultOutput{}, options).(LookupKatelloSyncPlanResultOutput), nil
		}).(LookupKatelloSyncPlanResultOutput)
}

// A collection of arguments for invoking getKatelloSyncPlan.
type LookupKatelloSyncPlanOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupKatelloSyncPlanOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKatelloSyncPlanArgs)(nil)).Elem()
}

// A collection of values returned by getKatelloSyncPlan.
type LookupKatelloSyncPlanResultOutput struct{ *pulumi.OutputState }

func (LookupKatelloSyncPlanResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKatelloSyncPlanResult)(nil)).Elem()
}

func (o LookupKatelloSyncPlanResultOutput) ToLookupKatelloSyncPlanResultOutput() LookupKatelloSyncPlanResultOutput {
	return o
}

func (o LookupKatelloSyncPlanResultOutput) ToLookupKatelloSyncPlanResultOutputWithContext(ctx context.Context) LookupKatelloSyncPlanResultOutput {
	return o
}

func (o LookupKatelloSyncPlanResultOutput) CronExpression() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloSyncPlanResult) string { return v.CronExpression }).(pulumi.StringOutput)
}

func (o LookupKatelloSyncPlanResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloSyncPlanResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupKatelloSyncPlanResultOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKatelloSyncPlanResult) bool { return v.Enabled }).(pulumi.BoolOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupKatelloSyncPlanResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloSyncPlanResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupKatelloSyncPlanResultOutput) Interval() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloSyncPlanResult) string { return v.Interval }).(pulumi.StringOutput)
}

func (o LookupKatelloSyncPlanResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloSyncPlanResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupKatelloSyncPlanResultOutput) SyncDate() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloSyncPlanResult) string { return v.SyncDate }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupKatelloSyncPlanResultOutput{})
}
