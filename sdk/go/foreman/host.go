// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Host struct {
	pulumi.CustomResourceState

	// @SUMMARY A host managed by Foreman.
	__meta_ pulumi.BoolOutput `pulumi:"__meta_"`
	// ID of the architecture of this host
	ArchitectureId pulumi.IntOutput `pulumi:"architectureId"`
	// Deprecated: The feature no longer exists
	BmcSuccess pulumi.BoolPtrOutput `pulumi:"bmcSuccess"`
	// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
	Comment pulumi.StringOutput `pulumi:"comment"`
	// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
	ComputeAttributes pulumi.StringOutput `pulumi:"computeAttributes"`
	ComputeProfileId  pulumi.IntOutput    `pulumi:"computeProfileId"`
	ComputeResourceId pulumi.IntOutput    `pulumi:"computeResourceId"`
	// IDs of the applied config groups.
	ConfigGroupIds pulumi.IntArrayOutput `pulumi:"configGroupIds"`
	// ID of the domain to assign to the host.
	DomainId pulumi.IntOutput `pulumi:"domainId"`
	// The domain name of the host.
	DomainName pulumi.StringOutput `pulumi:"domainName"`
	// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
	// boot to PXE and power on. Defaults to `false`.
	EnableBmc pulumi.BoolPtrOutput `pulumi:"enableBmc"`
	// ID of the environment to assign to the host.
	EnvironmentId pulumi.IntOutput `pulumi:"environmentId"`
	// Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
	Fqdn pulumi.StringOutput `pulumi:"fqdn"`
	// ID of the hostgroup to assign to the host.
	HostgroupId pulumi.IntOutput `pulumi:"hostgroupId"`
	// ID of an image to be used as base for this host when cloning
	ImageId pulumi.IntOutput `pulumi:"imageId"`
	// Host interface information.
	InterfacesAttributes HostInterfacesAttributeArrayOutput `pulumi:"interfacesAttributes"`
	// NAME of the location to assign to the host.
	LocationName pulumi.StringPtrOutput `pulumi:"locationName"`
	// Manage power operations, e.g. power on, if host's build flag will be enabled.
	ManagePowerOperations pulumi.BoolPtrOutput `pulumi:"managePowerOperations"`
	// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
	Managed pulumi.BoolPtrOutput `pulumi:"managed"`
	// ID of the medium mounted on the host.
	MediumId pulumi.IntOutput `pulumi:"mediumId"`
	// ID of the hardware model if applicable
	ModelId pulumi.IntOutput `pulumi:"modelId"`
	// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
	// setting 'append_domain_name_for_hosts').
	Name pulumi.StringOutput `pulumi:"name"`
	// ID of the operating system to put on the host.
	OperatingsystemId pulumi.IntOutput `pulumi:"operatingsystemId"`
	// NAME of the organization to assign to the host.
	OrganizationName pulumi.StringPtrOutput `pulumi:"organizationName"`
	// ID of the user or usergroup that owns the host.
	OwnerId pulumi.IntOutput `pulumi:"ownerId"`
	// Owner of the host, must be either User ot Usergroup
	OwnerType pulumi.StringOutput `pulumi:"ownerType"`
	// A map of parameters that will be saved as host parameters in the machine config.
	Parameters pulumi.StringMapOutput `pulumi:"parameters"`
	// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
	ProvisionMethod pulumi.StringPtrOutput `pulumi:"provisionMethod"`
	// ID of the partition table the host should use
	PtableId pulumi.IntOutput `pulumi:"ptableId"`
	// IDs of the applied puppet classes.
	PuppetClassIds pulumi.IntArrayOutput `pulumi:"puppetClassIds"`
	// Number of times to retry on a failed attempt to register or delete a host in foreman.
	RetryCount pulumi.IntPtrOutput `pulumi:"retryCount"`
	// Default root password
	RootPassword pulumi.StringPtrOutput `pulumi:"rootPassword"`
	// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
	SetBuildFlag pulumi.BoolPtrOutput `pulumi:"setBuildFlag"`
	// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
	Shortname pulumi.StringOutput `pulumi:"shortname"`
	// ID of the subnet the host should be placed in
	SubnetId pulumi.IntOutput `pulumi:"subnetId"`
	// Build token. Can be used to signal to Foreman that a host build is complete.
	Token pulumi.StringOutput `pulumi:"token"`
}

// NewHost registers a new resource with the given unique name, arguments, and options.
func NewHost(ctx *pulumi.Context,
	name string, args *HostArgs, opts ...pulumi.ResourceOption) (*Host, error) {
	if args == nil {
		args = &HostArgs{}
	}

	if args.RootPassword != nil {
		args.RootPassword = pulumi.ToSecret(args.RootPassword).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"rootPassword",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Host
	err := ctx.RegisterResource("foreman:index/host:Host", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHost gets an existing Host resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHost(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HostState, opts ...pulumi.ResourceOption) (*Host, error) {
	var resource Host
	err := ctx.ReadResource("foreman:index/host:Host", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Host resources.
type hostState struct {
	// @SUMMARY A host managed by Foreman.
	__meta_ *bool `pulumi:"__meta_"`
	// ID of the architecture of this host
	ArchitectureId *int `pulumi:"architectureId"`
	// Deprecated: The feature no longer exists
	BmcSuccess *bool `pulumi:"bmcSuccess"`
	// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
	Comment *string `pulumi:"comment"`
	// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
	ComputeAttributes *string `pulumi:"computeAttributes"`
	ComputeProfileId  *int    `pulumi:"computeProfileId"`
	ComputeResourceId *int    `pulumi:"computeResourceId"`
	// IDs of the applied config groups.
	ConfigGroupIds []int `pulumi:"configGroupIds"`
	// ID of the domain to assign to the host.
	DomainId *int `pulumi:"domainId"`
	// The domain name of the host.
	DomainName *string `pulumi:"domainName"`
	// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
	// boot to PXE and power on. Defaults to `false`.
	EnableBmc *bool `pulumi:"enableBmc"`
	// ID of the environment to assign to the host.
	EnvironmentId *int `pulumi:"environmentId"`
	// Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
	Fqdn *string `pulumi:"fqdn"`
	// ID of the hostgroup to assign to the host.
	HostgroupId *int `pulumi:"hostgroupId"`
	// ID of an image to be used as base for this host when cloning
	ImageId *int `pulumi:"imageId"`
	// Host interface information.
	InterfacesAttributes []HostInterfacesAttribute `pulumi:"interfacesAttributes"`
	// NAME of the location to assign to the host.
	LocationName *string `pulumi:"locationName"`
	// Manage power operations, e.g. power on, if host's build flag will be enabled.
	ManagePowerOperations *bool `pulumi:"managePowerOperations"`
	// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
	Managed *bool `pulumi:"managed"`
	// ID of the medium mounted on the host.
	MediumId *int `pulumi:"mediumId"`
	// ID of the hardware model if applicable
	ModelId *int `pulumi:"modelId"`
	// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
	// setting 'append_domain_name_for_hosts').
	Name *string `pulumi:"name"`
	// ID of the operating system to put on the host.
	OperatingsystemId *int `pulumi:"operatingsystemId"`
	// NAME of the organization to assign to the host.
	OrganizationName *string `pulumi:"organizationName"`
	// ID of the user or usergroup that owns the host.
	OwnerId *int `pulumi:"ownerId"`
	// Owner of the host, must be either User ot Usergroup
	OwnerType *string `pulumi:"ownerType"`
	// A map of parameters that will be saved as host parameters in the machine config.
	Parameters map[string]string `pulumi:"parameters"`
	// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
	ProvisionMethod *string `pulumi:"provisionMethod"`
	// ID of the partition table the host should use
	PtableId *int `pulumi:"ptableId"`
	// IDs of the applied puppet classes.
	PuppetClassIds []int `pulumi:"puppetClassIds"`
	// Number of times to retry on a failed attempt to register or delete a host in foreman.
	RetryCount *int `pulumi:"retryCount"`
	// Default root password
	RootPassword *string `pulumi:"rootPassword"`
	// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
	SetBuildFlag *bool `pulumi:"setBuildFlag"`
	// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
	Shortname *string `pulumi:"shortname"`
	// ID of the subnet the host should be placed in
	SubnetId *int `pulumi:"subnetId"`
	// Build token. Can be used to signal to Foreman that a host build is complete.
	Token *string `pulumi:"token"`
}

type HostState struct {
	// @SUMMARY A host managed by Foreman.
	__meta_ pulumi.BoolPtrInput
	// ID of the architecture of this host
	ArchitectureId pulumi.IntPtrInput
	// Deprecated: The feature no longer exists
	BmcSuccess pulumi.BoolPtrInput
	// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
	Comment pulumi.StringPtrInput
	// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
	ComputeAttributes pulumi.StringPtrInput
	ComputeProfileId  pulumi.IntPtrInput
	ComputeResourceId pulumi.IntPtrInput
	// IDs of the applied config groups.
	ConfigGroupIds pulumi.IntArrayInput
	// ID of the domain to assign to the host.
	DomainId pulumi.IntPtrInput
	// The domain name of the host.
	DomainName pulumi.StringPtrInput
	// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
	// boot to PXE and power on. Defaults to `false`.
	EnableBmc pulumi.BoolPtrInput
	// ID of the environment to assign to the host.
	EnvironmentId pulumi.IntPtrInput
	// Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
	Fqdn pulumi.StringPtrInput
	// ID of the hostgroup to assign to the host.
	HostgroupId pulumi.IntPtrInput
	// ID of an image to be used as base for this host when cloning
	ImageId pulumi.IntPtrInput
	// Host interface information.
	InterfacesAttributes HostInterfacesAttributeArrayInput
	// NAME of the location to assign to the host.
	LocationName pulumi.StringPtrInput
	// Manage power operations, e.g. power on, if host's build flag will be enabled.
	ManagePowerOperations pulumi.BoolPtrInput
	// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
	Managed pulumi.BoolPtrInput
	// ID of the medium mounted on the host.
	MediumId pulumi.IntPtrInput
	// ID of the hardware model if applicable
	ModelId pulumi.IntPtrInput
	// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
	// setting 'append_domain_name_for_hosts').
	Name pulumi.StringPtrInput
	// ID of the operating system to put on the host.
	OperatingsystemId pulumi.IntPtrInput
	// NAME of the organization to assign to the host.
	OrganizationName pulumi.StringPtrInput
	// ID of the user or usergroup that owns the host.
	OwnerId pulumi.IntPtrInput
	// Owner of the host, must be either User ot Usergroup
	OwnerType pulumi.StringPtrInput
	// A map of parameters that will be saved as host parameters in the machine config.
	Parameters pulumi.StringMapInput
	// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
	ProvisionMethod pulumi.StringPtrInput
	// ID of the partition table the host should use
	PtableId pulumi.IntPtrInput
	// IDs of the applied puppet classes.
	PuppetClassIds pulumi.IntArrayInput
	// Number of times to retry on a failed attempt to register or delete a host in foreman.
	RetryCount pulumi.IntPtrInput
	// Default root password
	RootPassword pulumi.StringPtrInput
	// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
	SetBuildFlag pulumi.BoolPtrInput
	// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
	Shortname pulumi.StringPtrInput
	// ID of the subnet the host should be placed in
	SubnetId pulumi.IntPtrInput
	// Build token. Can be used to signal to Foreman that a host build is complete.
	Token pulumi.StringPtrInput
}

func (HostState) ElementType() reflect.Type {
	return reflect.TypeOf((*hostState)(nil)).Elem()
}

type hostArgs struct {
	// ID of the architecture of this host
	ArchitectureId *int `pulumi:"architectureId"`
	// Deprecated: The feature no longer exists
	BmcSuccess *bool `pulumi:"bmcSuccess"`
	// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
	Comment *string `pulumi:"comment"`
	// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
	ComputeAttributes *string `pulumi:"computeAttributes"`
	ComputeProfileId  *int    `pulumi:"computeProfileId"`
	ComputeResourceId *int    `pulumi:"computeResourceId"`
	// IDs of the applied config groups.
	ConfigGroupIds []int `pulumi:"configGroupIds"`
	// ID of the domain to assign to the host.
	DomainId *int `pulumi:"domainId"`
	// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
	// boot to PXE and power on. Defaults to `false`.
	EnableBmc *bool `pulumi:"enableBmc"`
	// ID of the environment to assign to the host.
	EnvironmentId *int `pulumi:"environmentId"`
	// ID of the hostgroup to assign to the host.
	HostgroupId *int `pulumi:"hostgroupId"`
	// ID of an image to be used as base for this host when cloning
	ImageId *int `pulumi:"imageId"`
	// Host interface information.
	InterfacesAttributes []HostInterfacesAttribute `pulumi:"interfacesAttributes"`
	// NAME of the location to assign to the host.
	LocationName *string `pulumi:"locationName"`
	// Manage power operations, e.g. power on, if host's build flag will be enabled.
	ManagePowerOperations *bool `pulumi:"managePowerOperations"`
	// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
	Managed *bool `pulumi:"managed"`
	// ID of the medium mounted on the host.
	MediumId *int `pulumi:"mediumId"`
	// ID of the hardware model if applicable
	ModelId *int `pulumi:"modelId"`
	// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
	// setting 'append_domain_name_for_hosts').
	Name *string `pulumi:"name"`
	// ID of the operating system to put on the host.
	OperatingsystemId *int `pulumi:"operatingsystemId"`
	// NAME of the organization to assign to the host.
	OrganizationName *string `pulumi:"organizationName"`
	// ID of the user or usergroup that owns the host.
	OwnerId *int `pulumi:"ownerId"`
	// Owner of the host, must be either User ot Usergroup
	OwnerType *string `pulumi:"ownerType"`
	// A map of parameters that will be saved as host parameters in the machine config.
	Parameters map[string]string `pulumi:"parameters"`
	// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
	ProvisionMethod *string `pulumi:"provisionMethod"`
	// ID of the partition table the host should use
	PtableId *int `pulumi:"ptableId"`
	// IDs of the applied puppet classes.
	PuppetClassIds []int `pulumi:"puppetClassIds"`
	// Number of times to retry on a failed attempt to register or delete a host in foreman.
	RetryCount *int `pulumi:"retryCount"`
	// Default root password
	RootPassword *string `pulumi:"rootPassword"`
	// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
	SetBuildFlag *bool `pulumi:"setBuildFlag"`
	// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
	Shortname *string `pulumi:"shortname"`
	// ID of the subnet the host should be placed in
	SubnetId *int `pulumi:"subnetId"`
}

// The set of arguments for constructing a Host resource.
type HostArgs struct {
	// ID of the architecture of this host
	ArchitectureId pulumi.IntPtrInput
	// Deprecated: The feature no longer exists
	BmcSuccess pulumi.BoolPtrInput
	// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
	Comment pulumi.StringPtrInput
	// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
	ComputeAttributes pulumi.StringPtrInput
	ComputeProfileId  pulumi.IntPtrInput
	ComputeResourceId pulumi.IntPtrInput
	// IDs of the applied config groups.
	ConfigGroupIds pulumi.IntArrayInput
	// ID of the domain to assign to the host.
	DomainId pulumi.IntPtrInput
	// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
	// boot to PXE and power on. Defaults to `false`.
	EnableBmc pulumi.BoolPtrInput
	// ID of the environment to assign to the host.
	EnvironmentId pulumi.IntPtrInput
	// ID of the hostgroup to assign to the host.
	HostgroupId pulumi.IntPtrInput
	// ID of an image to be used as base for this host when cloning
	ImageId pulumi.IntPtrInput
	// Host interface information.
	InterfacesAttributes HostInterfacesAttributeArrayInput
	// NAME of the location to assign to the host.
	LocationName pulumi.StringPtrInput
	// Manage power operations, e.g. power on, if host's build flag will be enabled.
	ManagePowerOperations pulumi.BoolPtrInput
	// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
	Managed pulumi.BoolPtrInput
	// ID of the medium mounted on the host.
	MediumId pulumi.IntPtrInput
	// ID of the hardware model if applicable
	ModelId pulumi.IntPtrInput
	// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
	// setting 'append_domain_name_for_hosts').
	Name pulumi.StringPtrInput
	// ID of the operating system to put on the host.
	OperatingsystemId pulumi.IntPtrInput
	// NAME of the organization to assign to the host.
	OrganizationName pulumi.StringPtrInput
	// ID of the user or usergroup that owns the host.
	OwnerId pulumi.IntPtrInput
	// Owner of the host, must be either User ot Usergroup
	OwnerType pulumi.StringPtrInput
	// A map of parameters that will be saved as host parameters in the machine config.
	Parameters pulumi.StringMapInput
	// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
	ProvisionMethod pulumi.StringPtrInput
	// ID of the partition table the host should use
	PtableId pulumi.IntPtrInput
	// IDs of the applied puppet classes.
	PuppetClassIds pulumi.IntArrayInput
	// Number of times to retry on a failed attempt to register or delete a host in foreman.
	RetryCount pulumi.IntPtrInput
	// Default root password
	RootPassword pulumi.StringPtrInput
	// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
	SetBuildFlag pulumi.BoolPtrInput
	// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
	Shortname pulumi.StringPtrInput
	// ID of the subnet the host should be placed in
	SubnetId pulumi.IntPtrInput
}

func (HostArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hostArgs)(nil)).Elem()
}

type HostInput interface {
	pulumi.Input

	ToHostOutput() HostOutput
	ToHostOutputWithContext(ctx context.Context) HostOutput
}

func (*Host) ElementType() reflect.Type {
	return reflect.TypeOf((**Host)(nil)).Elem()
}

func (i *Host) ToHostOutput() HostOutput {
	return i.ToHostOutputWithContext(context.Background())
}

func (i *Host) ToHostOutputWithContext(ctx context.Context) HostOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HostOutput)
}

// HostArrayInput is an input type that accepts HostArray and HostArrayOutput values.
// You can construct a concrete instance of `HostArrayInput` via:
//
//	HostArray{ HostArgs{...} }
type HostArrayInput interface {
	pulumi.Input

	ToHostArrayOutput() HostArrayOutput
	ToHostArrayOutputWithContext(context.Context) HostArrayOutput
}

type HostArray []HostInput

func (HostArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Host)(nil)).Elem()
}

func (i HostArray) ToHostArrayOutput() HostArrayOutput {
	return i.ToHostArrayOutputWithContext(context.Background())
}

func (i HostArray) ToHostArrayOutputWithContext(ctx context.Context) HostArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HostArrayOutput)
}

// HostMapInput is an input type that accepts HostMap and HostMapOutput values.
// You can construct a concrete instance of `HostMapInput` via:
//
//	HostMap{ "key": HostArgs{...} }
type HostMapInput interface {
	pulumi.Input

	ToHostMapOutput() HostMapOutput
	ToHostMapOutputWithContext(context.Context) HostMapOutput
}

type HostMap map[string]HostInput

func (HostMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Host)(nil)).Elem()
}

func (i HostMap) ToHostMapOutput() HostMapOutput {
	return i.ToHostMapOutputWithContext(context.Background())
}

func (i HostMap) ToHostMapOutputWithContext(ctx context.Context) HostMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HostMapOutput)
}

type HostOutput struct{ *pulumi.OutputState }

func (HostOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Host)(nil)).Elem()
}

func (o HostOutput) ToHostOutput() HostOutput {
	return o
}

func (o HostOutput) ToHostOutputWithContext(ctx context.Context) HostOutput {
	return o
}

// @SUMMARY A host managed by Foreman.
func (o HostOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *Host) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

// ID of the architecture of this host
func (o HostOutput) ArchitectureId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.ArchitectureId }).(pulumi.IntOutput)
}

// Deprecated: The feature no longer exists
func (o HostOutput) BmcSuccess() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.BoolPtrOutput { return v.BmcSuccess }).(pulumi.BoolPtrOutput)
}

// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
func (o HostOutput) Comment() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.Comment }).(pulumi.StringOutput)
}

// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
func (o HostOutput) ComputeAttributes() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.ComputeAttributes }).(pulumi.StringOutput)
}

func (o HostOutput) ComputeProfileId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.ComputeProfileId }).(pulumi.IntOutput)
}

func (o HostOutput) ComputeResourceId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.ComputeResourceId }).(pulumi.IntOutput)
}

// IDs of the applied config groups.
func (o HostOutput) ConfigGroupIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Host) pulumi.IntArrayOutput { return v.ConfigGroupIds }).(pulumi.IntArrayOutput)
}

// ID of the domain to assign to the host.
func (o HostOutput) DomainId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.DomainId }).(pulumi.IntOutput)
}

// The domain name of the host.
func (o HostOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.DomainName }).(pulumi.StringOutput)
}

// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
// boot to PXE and power on. Defaults to `false`.
func (o HostOutput) EnableBmc() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.BoolPtrOutput { return v.EnableBmc }).(pulumi.BoolPtrOutput)
}

// ID of the environment to assign to the host.
func (o HostOutput) EnvironmentId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.EnvironmentId }).(pulumi.IntOutput)
}

// Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
func (o HostOutput) Fqdn() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.Fqdn }).(pulumi.StringOutput)
}

// ID of the hostgroup to assign to the host.
func (o HostOutput) HostgroupId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.HostgroupId }).(pulumi.IntOutput)
}

// ID of an image to be used as base for this host when cloning
func (o HostOutput) ImageId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.ImageId }).(pulumi.IntOutput)
}

// Host interface information.
func (o HostOutput) InterfacesAttributes() HostInterfacesAttributeArrayOutput {
	return o.ApplyT(func(v *Host) HostInterfacesAttributeArrayOutput { return v.InterfacesAttributes }).(HostInterfacesAttributeArrayOutput)
}

// NAME of the location to assign to the host.
func (o HostOutput) LocationName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.StringPtrOutput { return v.LocationName }).(pulumi.StringPtrOutput)
}

// Manage power operations, e.g. power on, if host's build flag will be enabled.
func (o HostOutput) ManagePowerOperations() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.BoolPtrOutput { return v.ManagePowerOperations }).(pulumi.BoolPtrOutput)
}

// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
func (o HostOutput) Managed() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.BoolPtrOutput { return v.Managed }).(pulumi.BoolPtrOutput)
}

// ID of the medium mounted on the host.
func (o HostOutput) MediumId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.MediumId }).(pulumi.IntOutput)
}

// ID of the hardware model if applicable
func (o HostOutput) ModelId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.ModelId }).(pulumi.IntOutput)
}

// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
// setting 'append_domain_name_for_hosts').
func (o HostOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// ID of the operating system to put on the host.
func (o HostOutput) OperatingsystemId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.OperatingsystemId }).(pulumi.IntOutput)
}

// NAME of the organization to assign to the host.
func (o HostOutput) OrganizationName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.StringPtrOutput { return v.OrganizationName }).(pulumi.StringPtrOutput)
}

// ID of the user or usergroup that owns the host.
func (o HostOutput) OwnerId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.OwnerId }).(pulumi.IntOutput)
}

// Owner of the host, must be either User ot Usergroup
func (o HostOutput) OwnerType() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.OwnerType }).(pulumi.StringOutput)
}

// A map of parameters that will be saved as host parameters in the machine config.
func (o HostOutput) Parameters() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Host) pulumi.StringMapOutput { return v.Parameters }).(pulumi.StringMapOutput)
}

// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
func (o HostOutput) ProvisionMethod() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.StringPtrOutput { return v.ProvisionMethod }).(pulumi.StringPtrOutput)
}

// ID of the partition table the host should use
func (o HostOutput) PtableId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.PtableId }).(pulumi.IntOutput)
}

// IDs of the applied puppet classes.
func (o HostOutput) PuppetClassIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Host) pulumi.IntArrayOutput { return v.PuppetClassIds }).(pulumi.IntArrayOutput)
}

// Number of times to retry on a failed attempt to register or delete a host in foreman.
func (o HostOutput) RetryCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.IntPtrOutput { return v.RetryCount }).(pulumi.IntPtrOutput)
}

// Default root password
func (o HostOutput) RootPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.StringPtrOutput { return v.RootPassword }).(pulumi.StringPtrOutput)
}

// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
func (o HostOutput) SetBuildFlag() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Host) pulumi.BoolPtrOutput { return v.SetBuildFlag }).(pulumi.BoolPtrOutput)
}

// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
func (o HostOutput) Shortname() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.Shortname }).(pulumi.StringOutput)
}

// ID of the subnet the host should be placed in
func (o HostOutput) SubnetId() pulumi.IntOutput {
	return o.ApplyT(func(v *Host) pulumi.IntOutput { return v.SubnetId }).(pulumi.IntOutput)
}

// Build token. Can be used to signal to Foreman that a host build is complete.
func (o HostOutput) Token() pulumi.StringOutput {
	return o.ApplyT(func(v *Host) pulumi.StringOutput { return v.Token }).(pulumi.StringOutput)
}

type HostArrayOutput struct{ *pulumi.OutputState }

func (HostArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Host)(nil)).Elem()
}

func (o HostArrayOutput) ToHostArrayOutput() HostArrayOutput {
	return o
}

func (o HostArrayOutput) ToHostArrayOutputWithContext(ctx context.Context) HostArrayOutput {
	return o
}

func (o HostArrayOutput) Index(i pulumi.IntInput) HostOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Host {
		return vs[0].([]*Host)[vs[1].(int)]
	}).(HostOutput)
}

type HostMapOutput struct{ *pulumi.OutputState }

func (HostMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Host)(nil)).Elem()
}

func (o HostMapOutput) ToHostMapOutput() HostMapOutput {
	return o
}

func (o HostMapOutput) ToHostMapOutputWithContext(ctx context.Context) HostMapOutput {
	return o
}

func (o HostMapOutput) MapIndex(k pulumi.StringInput) HostOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Host {
		return vs[0].(map[string]*Host)[vs[1].(string)]
	}).(HostOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HostInput)(nil)).Elem(), &Host{})
	pulumi.RegisterInputType(reflect.TypeOf((*HostArrayInput)(nil)).Elem(), HostArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*HostMapInput)(nil)).Elem(), HostMap{})
	pulumi.RegisterOutputType(HostOutput{})
	pulumi.RegisterOutputType(HostArrayOutput{})
	pulumi.RegisterOutputType(HostMapOutput{})
}
