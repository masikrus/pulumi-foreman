// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"errors"
	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type OverrideValue struct {
	pulumi.CustomResourceState

	// @SUMMARY Smart class parameter override value.
	__meta_ pulumi.BoolOutput `pulumi:"__meta_"`
	// A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
	// `domain` or `os`@EXAMPLE { type = "hostgroup" value = "exampleGroup" }
	Match pulumi.StringMapOutput `pulumi:"match"`
	// When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
	// false
	Omit pulumi.BoolPtrOutput `pulumi:"omit"`
	// ID of the smart class parameter to override.@EXAMPLE 1
	SmartClassParameterId pulumi.IntOutput `pulumi:"smartClassParameterId"`
	// Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewOverrideValue registers a new resource with the given unique name, arguments, and options.
func NewOverrideValue(ctx *pulumi.Context,
	name string, args *OverrideValueArgs, opts ...pulumi.ResourceOption) (*OverrideValue, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Match == nil {
		return nil, errors.New("invalid value for required argument 'Match'")
	}
	if args.SmartClassParameterId == nil {
		return nil, errors.New("invalid value for required argument 'SmartClassParameterId'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OverrideValue
	err := ctx.RegisterResource("foreman:index/overrideValue:OverrideValue", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOverrideValue gets an existing OverrideValue resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOverrideValue(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OverrideValueState, opts ...pulumi.ResourceOption) (*OverrideValue, error) {
	var resource OverrideValue
	err := ctx.ReadResource("foreman:index/overrideValue:OverrideValue", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OverrideValue resources.
type overrideValueState struct {
	// @SUMMARY Smart class parameter override value.
	__meta_ *bool `pulumi:"__meta_"`
	// A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
	// `domain` or `os`@EXAMPLE { type = "hostgroup" value = "exampleGroup" }
	Match map[string]string `pulumi:"match"`
	// When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
	// false
	Omit *bool `pulumi:"omit"`
	// ID of the smart class parameter to override.@EXAMPLE 1
	SmartClassParameterId *int `pulumi:"smartClassParameterId"`
	// Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
	Value *string `pulumi:"value"`
}

type OverrideValueState struct {
	// @SUMMARY Smart class parameter override value.
	__meta_ pulumi.BoolPtrInput
	// A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
	// `domain` or `os`@EXAMPLE { type = "hostgroup" value = "exampleGroup" }
	Match pulumi.StringMapInput
	// When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
	// false
	Omit pulumi.BoolPtrInput
	// ID of the smart class parameter to override.@EXAMPLE 1
	SmartClassParameterId pulumi.IntPtrInput
	// Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
	Value pulumi.StringPtrInput
}

func (OverrideValueState) ElementType() reflect.Type {
	return reflect.TypeOf((*overrideValueState)(nil)).Elem()
}

type overrideValueArgs struct {
	// A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
	// `domain` or `os`@EXAMPLE { type = "hostgroup" value = "exampleGroup" }
	Match map[string]string `pulumi:"match"`
	// When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
	// false
	Omit *bool `pulumi:"omit"`
	// ID of the smart class parameter to override.@EXAMPLE 1
	SmartClassParameterId int `pulumi:"smartClassParameterId"`
	// Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a OverrideValue resource.
type OverrideValueArgs struct {
	// A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
	// `domain` or `os`@EXAMPLE { type = "hostgroup" value = "exampleGroup" }
	Match pulumi.StringMapInput
	// When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
	// false
	Omit pulumi.BoolPtrInput
	// ID of the smart class parameter to override.@EXAMPLE 1
	SmartClassParameterId pulumi.IntInput
	// Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
	Value pulumi.StringInput
}

func (OverrideValueArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*overrideValueArgs)(nil)).Elem()
}

type OverrideValueInput interface {
	pulumi.Input

	ToOverrideValueOutput() OverrideValueOutput
	ToOverrideValueOutputWithContext(ctx context.Context) OverrideValueOutput
}

func (*OverrideValue) ElementType() reflect.Type {
	return reflect.TypeOf((**OverrideValue)(nil)).Elem()
}

func (i *OverrideValue) ToOverrideValueOutput() OverrideValueOutput {
	return i.ToOverrideValueOutputWithContext(context.Background())
}

func (i *OverrideValue) ToOverrideValueOutputWithContext(ctx context.Context) OverrideValueOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OverrideValueOutput)
}

// OverrideValueArrayInput is an input type that accepts OverrideValueArray and OverrideValueArrayOutput values.
// You can construct a concrete instance of `OverrideValueArrayInput` via:
//
//	OverrideValueArray{ OverrideValueArgs{...} }
type OverrideValueArrayInput interface {
	pulumi.Input

	ToOverrideValueArrayOutput() OverrideValueArrayOutput
	ToOverrideValueArrayOutputWithContext(context.Context) OverrideValueArrayOutput
}

type OverrideValueArray []OverrideValueInput

func (OverrideValueArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OverrideValue)(nil)).Elem()
}

func (i OverrideValueArray) ToOverrideValueArrayOutput() OverrideValueArrayOutput {
	return i.ToOverrideValueArrayOutputWithContext(context.Background())
}

func (i OverrideValueArray) ToOverrideValueArrayOutputWithContext(ctx context.Context) OverrideValueArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OverrideValueArrayOutput)
}

// OverrideValueMapInput is an input type that accepts OverrideValueMap and OverrideValueMapOutput values.
// You can construct a concrete instance of `OverrideValueMapInput` via:
//
//	OverrideValueMap{ "key": OverrideValueArgs{...} }
type OverrideValueMapInput interface {
	pulumi.Input

	ToOverrideValueMapOutput() OverrideValueMapOutput
	ToOverrideValueMapOutputWithContext(context.Context) OverrideValueMapOutput
}

type OverrideValueMap map[string]OverrideValueInput

func (OverrideValueMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OverrideValue)(nil)).Elem()
}

func (i OverrideValueMap) ToOverrideValueMapOutput() OverrideValueMapOutput {
	return i.ToOverrideValueMapOutputWithContext(context.Background())
}

func (i OverrideValueMap) ToOverrideValueMapOutputWithContext(ctx context.Context) OverrideValueMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OverrideValueMapOutput)
}

type OverrideValueOutput struct{ *pulumi.OutputState }

func (OverrideValueOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OverrideValue)(nil)).Elem()
}

func (o OverrideValueOutput) ToOverrideValueOutput() OverrideValueOutput {
	return o
}

func (o OverrideValueOutput) ToOverrideValueOutputWithContext(ctx context.Context) OverrideValueOutput {
	return o
}

// @SUMMARY Smart class parameter override value.
func (o OverrideValueOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *OverrideValue) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

// A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
// `domain` or `os`@EXAMPLE { type = "hostgroup" value = "exampleGroup" }
func (o OverrideValueOutput) Match() pulumi.StringMapOutput {
	return o.ApplyT(func(v *OverrideValue) pulumi.StringMapOutput { return v.Match }).(pulumi.StringMapOutput)
}

// When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
// false
func (o OverrideValueOutput) Omit() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *OverrideValue) pulumi.BoolPtrOutput { return v.Omit }).(pulumi.BoolPtrOutput)
}

// ID of the smart class parameter to override.@EXAMPLE 1
func (o OverrideValueOutput) SmartClassParameterId() pulumi.IntOutput {
	return o.ApplyT(func(v *OverrideValue) pulumi.IntOutput { return v.SmartClassParameterId }).(pulumi.IntOutput)
}

// Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
func (o OverrideValueOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *OverrideValue) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

type OverrideValueArrayOutput struct{ *pulumi.OutputState }

func (OverrideValueArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OverrideValue)(nil)).Elem()
}

func (o OverrideValueArrayOutput) ToOverrideValueArrayOutput() OverrideValueArrayOutput {
	return o
}

func (o OverrideValueArrayOutput) ToOverrideValueArrayOutputWithContext(ctx context.Context) OverrideValueArrayOutput {
	return o
}

func (o OverrideValueArrayOutput) Index(i pulumi.IntInput) OverrideValueOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OverrideValue {
		return vs[0].([]*OverrideValue)[vs[1].(int)]
	}).(OverrideValueOutput)
}

type OverrideValueMapOutput struct{ *pulumi.OutputState }

func (OverrideValueMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OverrideValue)(nil)).Elem()
}

func (o OverrideValueMapOutput) ToOverrideValueMapOutput() OverrideValueMapOutput {
	return o
}

func (o OverrideValueMapOutput) ToOverrideValueMapOutputWithContext(ctx context.Context) OverrideValueMapOutput {
	return o
}

func (o OverrideValueMapOutput) MapIndex(k pulumi.StringInput) OverrideValueOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OverrideValue {
		return vs[0].(map[string]*OverrideValue)[vs[1].(string)]
	}).(OverrideValueOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OverrideValueInput)(nil)).Elem(), &OverrideValue{})
	pulumi.RegisterInputType(reflect.TypeOf((*OverrideValueArrayInput)(nil)).Elem(), OverrideValueArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OverrideValueMapInput)(nil)).Elem(), OverrideValueMap{})
	pulumi.RegisterOutputType(OverrideValueOutput{})
	pulumi.RegisterOutputType(OverrideValueArrayOutput{})
	pulumi.RegisterOutputType(OverrideValueMapOutput{})
}
