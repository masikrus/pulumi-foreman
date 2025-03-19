// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";

export interface ComputeprofileComputeAttribute {
    /**
     * ID of the compute resource
     */
    computeResourceId: number;
    /**
     * ID of the compute_attribute
     */
    id: number;
    /**
     * Auto-generated name of the compute attribute
     */
    name: string;
    /**
     * VM attributes as JSON
     */
    vmAttrs: {[key: string]: string};
}

export interface GetComputeprofileComputeAttribute {
    /**
     * ID of the compute resource
     */
    computeResourceId: number;
    /**
     * ID of the compute_attribute
     */
    id: number;
    /**
     * Auto-generated name of the compute attribute
     */
    name: string;
    /**
     * VM attributes as JSON
     */
    vmAttrs: {[key: string]: string};
}

export interface GetJobtemplateTemplateInput {
    /**
     * @SUMMARY Foreman representation of a template input.
     */
    __meta_: boolean;
    advanced: boolean;
    default: string;
    description: string;
    factName: string;
    hiddenValue: boolean;
    id: string;
    inputType: string;
    /**
     * The name of the template input
     */
    name: string;
    puppetClassName: string;
    puppetParameterName: string;
    required: boolean;
    resourceType: string;
    templateId: number;
    valueType: string;
    variableName: string;
}

export interface GetKatelloContentViewFilter {
    description: string;
    id: number;
    /**
     * specifies if content should be included or excluded, default: inclusion=false
     */
    inclusion: boolean;
    name: string;
    rules: outputs.GetKatelloContentViewFilterRule[];
    /**
     * Type of this filter, e.g. DEB or RPM
     */
    type: string;
}

export interface GetKatelloContentViewFilterRule {
    architecture: string;
    id: number;
    /**
     * Filter pattern of this filter @EXAMPLE apt*
     */
    name: string;
}

export interface GetProvisioningtemplateTemplateCombinationsAttribute {
    /**
     * The environment ID for this template combination.
     */
    environmentId: number;
    /**
     * The hostgroup ID for this template combination.
     */
    hostgroupId: number;
    /**
     * Template combination unique identifier.
     */
    id: number;
}

export interface HostInterfacesAttribute {
    /**
     * Identifiers of attached interfaces, e.g. 'eth1', 'eth2' as comma-separated list
     */
    attachedDevices?: string;
    /**
     * Identifier of the interface to which this interface belongs.
     */
    attachedTo?: string;
    /**
     * Provider used for BMC/IMPI functionality. Values include: `"IPMI"`
     */
    bmcProvider?: string;
    /**
     * Hypervisor specific interface options
     */
    computeAttributes?: {[key: string]: string};
    /**
     * Unique identifier for the interface.
     */
    id: number;
    /**
     * Identifier of this interface local to the host.
     */
    identifier?: string;
    /**
     * IP address associated with the interface.
     */
    ip: string;
    /**
     * MAC address associated with the interface.
     */
    mac: string;
    /**
     * Whether or not this interface is managed by Foreman.
     */
    managed?: boolean;
    /**
     * Name of the interface
     */
    name: string;
    /**
     * Associated password used for BMC/IPMI functionality.
     */
    password?: string;
    /**
     * Whether or not this is the primary interface.
     */
    primary?: boolean;
    /**
     * Whether or not this interface is used to provision the host.
     */
    provision?: boolean;
    /**
     * ID of the subnet to associate with this interface.
     */
    subnetId: number;
    /**
     * The type of interface. Values include: `"interface"`, `"bmc"`, `"bond"`, `"bridge"`.
     */
    type?: string;
    /**
     * Username used for BMC/IPMI functionality.
     */
    username?: string;
    /**
     * Whether or not this is a virtual interface.
     */
    virtual?: boolean;
}

export interface JobtemplateTemplateInput {
    /**
     * @SUMMARY Foreman representation of a template input.
     */
    __meta_: boolean;
    advanced?: boolean;
    default: string;
    description?: string;
    factName?: string;
    hiddenValue?: boolean;
    id: string;
    inputType?: string;
    /**
     * The name of the template input
     */
    name: string;
    puppetClassName?: string;
    puppetParameterName?: string;
    required?: boolean;
    resourceType?: string;
    templateId: number;
    valueType?: string;
    variableName?: string;
}

export interface KatelloContentViewFilter {
    description?: string;
    id: number;
    /**
     * specifies if content should be included or excluded, default: inclusion=false
     */
    inclusion?: boolean;
    name: string;
    rules?: outputs.KatelloContentViewFilterRule[];
    /**
     * Type of this filter, e.g. DEB or RPM
     */
    type: string;
}

export interface KatelloContentViewFilterRule {
    architecture?: string;
    id: number;
    /**
     * Filter pattern of this filter @EXAMPLE apt*
     */
    name: string;
}

export interface ProvisioningtemplateTemplateCombinationsAttribute {
    /**
     * The environment ID for this template combination.
     */
    environmentId: number;
    /**
     * The hostgroup ID for this template combination.
     */
    hostgroupId: number;
    /**
     * Template combination unique identifier.
     */
    id: number;
}

