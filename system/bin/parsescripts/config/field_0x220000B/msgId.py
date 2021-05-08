﻿#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      msgId.py
# * Description   list cttf msg
# * Version       1.0
# * Data          2016-07-08 create file
#***********************************************************************
cproc_cttf_hrpd_msg_enum_table = {
    0x4300 : "ID_CTTF_CPROC_HRPD_AC_CONFIG_REQ",
    0x4301 : "ID_CPROC_CTTF_HRPD_AC_CONFIG_CNF",
    0x4302 : "ID_CPROC_CTTF_HRPD_AC_PROBE_IND",
    0x4303 : "ID_CTTF_CPROC_HRPD_AC_RELEASE_REQ",
    0x4304 : "ID_CPROC_CTTF_HRPD_AC_RELEASE_CNF",
    0x4305 : "ID_CPROC_CTTF_HRPD_AC_ERROR_IND",
    0x4306 : "ID_CTTF_CPROC_HRPD_TCH_CONFIG_REQ",
    0x4307 : "ID_CPROC_CTTF_HRPD_TCH_CONFIG_CNF",
    0x4308 : "ID_CTTF_CPROC_HRPD_TCH_RECONFIG_REQ",
    0x4309 : "ID_CPROC_CTTF_HRPD_TCH_RECONFIG_CNF",
    0x430A : "ID_CTTF_CPROC_HRPD_DRC_MODE_REQ",
    0x430B : "ID_CPROC_CTTF_HRPD_DRC_MODE_CNF",
    0x430C : "ID_CTTF_CPROC_HRPD_TCH_RELEASE_REQ",
    0x430D : "ID_CPROC_CTTF_HRPD_TCH_RELEASE_CNF",
    0x430E : "ID_CPROC_CTTF_HRPD_SUSPENDED_IND",
    0x430F : "ID_CTTF_CPROC_HRPD_SUSPENDED_RSP",
    0x4310 : "ID_CPROC_CTTF_HRPD_RESUMED_IND",
}

cas_cttf_hrpd_msg_enum_tabel = {
    0x3400 :     "ID_CAS_CTTF_HRPD_SNP_RELEASE_ALL_REQ",           
    0x3401 :     "ID_CTTF_CAS_HRPD_SNP_RELEASE_ALL_CNF",           
    0x3402 :     "ID_CAS_CTTF_HRPD_SNP_CONNECTION_CLOSED_IND",     
    0x3403 :     "ID_CAS_CTTF_HRPD_SNP_CONNECTION_OPENED_IND",     
    0x3404 :     "ID_CAS_CTTF_HRPD_SNP_CONNECTION_INITIATED_IND",  
    0x3405 :     "ID_CTTF_CAS_HRPD_SNP_DATA_CNF",                  
    0x3406 :     "ID_CTTF_CAS_HRPD_SNP_OPEN_CONNECTION_REQ",       
    0x3407 :     "ID_CAS_CTTF_HRPD_SNP_DATA_REQ",                  
    0x3408 :     "ID_CTTF_CAS_HRPD_SNP_DATA_IND",                  
    0x3409 :     "ID_CTTF_CAS_HRPD_SNP_ERROR_IND",                 
    0x340A :     "ID_CAS_CTTF_HRPD_TX_STATUS_NOTIFY",              
    0x340B :     "ID_CAS_CTTF_HRPD_SNP_DATA_CANCEL_REQ",           
    0x340C :     "ID_CTTF_CAS_HRPD_SNP_DATA_STATE_IND",            
    0x3700 :     "ID_CAS_CTTF_HRPD_RSLP_RELEASE_ALL_REQ",          
    0x3701 :     "ID_CTTF_CAS_HRPD_RSLP_RELEASE_ALL_CNF",          
    0x3702 :     "ID_CTTF_CAS_HRPD_RSLP_ERROR_IND",                
    0x3703 :     "ID_CTTF_CAS_HRPD_RSLP_AC_SIG_TX_BEGIN_NTF",      
    0x3704 :     "ID_CTTF_CAS_HRPD_RSLP_AC_SIG_TX_END_NTF",        
    0x3200 :     "ID_CAS_CTTF_HRPD_MAC_RELEASE_ALL_REQ",           
    0x3201 :     "ID_CTTF_CAS_HRPD_MAC_RELEASE_ALL_CNF",           
    0x3202 :     "ID_CAS_CTTF_HRPD_SECTOR_ID_NTF",                 
    0x3203 :     "ID_CAS_CTTF_HRPD_CCMAC_ACTIVATE_REQ",            
    0x3204 :     "ID_CTTF_CAS_HRPD_CCMAC_ACTIVATE_CNF",            
    0x3205 :     "ID_CAS_CTTF_HRPD_CCMAC_DEACTIVATE_REQ",          
    0x3206 :     "ID_CTTF_CAS_HRPD_CCMAC_DEACTIVATE_CNF",          
    0x3207 :     "ID_CTTF_CAS_HRPD_CCMAC_SUPERVISION_FAILED_IND",  
    0x3208 :     "ID_CAS_CTTF_HRPD_TCHMAC_ACTIVATE_REQ",           
    0x3209 :     "ID_CTTF_CAS_HRPD_TCHMAC_ACTIVATE_CNF",           
    0x320A :     "ID_CAS_CTTF_HRPD_TCHMAC_RECONFIG_REQ",           
    0x320B :     "ID_CTTF_CAS_HRPD_TCHMAC_RECONFIG_CNF",           
    0x320C :     "ID_CAS_CTTF_HRPD_TCHMAC_DEACTIVATE_REQ",         
    0x320D :     "ID_CTTF_CAS_HRPD_TCHMAC_DEACTIVATE_CNF",         
    0x320E :     "ID_CTTF_CAS_HRPD_FTCMAC_SUPERVISION_FAILED_IND", 
    0x320F :     "ID_CAS_CTTF_HRPD_ACMAC_ACTIVATE_REQ",            
    0x3210 :     "ID_CTTF_CAS_HRPD_ACMAC_ACTIVATE_CNF",            
    0x3211 :     "ID_CAS_CTTF_HRPD_ACMAC_RECONFIG_REQ",            
    0x3212 :     "ID_CTTF_CAS_HRPD_ACMAC_RECONFIG_CNF",            
    0x3213 :     "ID_CAS_CTTF_HRPD_ACMAC_DEACTIVATE_REQ",          
    0x3214 :     "ID_CTTF_CAS_HRPD_ACMAC_DEACTIVATE_CNF",          
    0x3215 :     "ID_CTTF_CAS_HRPD_ACMAC_TRANSMISSION_ABORTED_IND",      
    0x3216 :     "ID_CAS_CTTF_HRPD_RMAC_COMMIT_NTF",                
    0x3217 :     "ID_CTTF_CAS_HRPD_MAC_ERROR_IND",                  
    0x3218 :     "ID_CAS_CTTF_HRPD_MAC_SESSION_CONFIG_UPDATE_NTF",  
    0x3219 :     "ID_CAS_CTTF_HRPD_CCMAC_EXCHANGE_NTF",             
    0x321A :     "ID_CAS_CTTF_HRPD_CCMAC_MONITOR_NTF",              
    0x321B :     "ID_CAS_CTTF_HRPD_ACMAC_PHASE_REQ",                
    0x321C :     "ID_CTTF_CAS_HRPD_ACMAC_PHASE_CNF",                
    0x321D :     "ID_CAS_CTTF_HRPD_ACMAC_CLEAR_PARA_REQ",           
    0x321E :     "ID_CTTF_CAS_HRPD_ACMAC_CLEAR_PARA_CNF",           
    0x321F :     "ID_CAS_CTTF_HRPD_ACMAC_TX_CTRL_REQ",              
    0x3220 :     "ID_CTTF_CAS_HRPD_ACMAC_TX_CTRL_CNF",              
    0x3221 :     "ID_CAS_CTTF_HRPD_MAC_TX_CTRL_REQ",                
    0x3222 :     "ID_CTTF_CAS_HRPD_MAC_TX_CTRL_CNF",
    0x3223 :     "ID_CAS_CTTF_HRPD_RF_PROTECT_INFO_IND",              
    0x3224 :     "ID_CTTF_CAS_HRPD_RF_PROTECT_START_IND",                
    0x3225 :     "ID_CTTF_CAS_HRPD_RF_PROTECT_STOP_IND",
    0x3800 :     "ID_CAS_CTTF_HRPD_SPS_RELEASE_ALL_REQ",            
    0x3801 :     "ID_CTTF_CAS_HRPD_SPS_RELEASE_ALL_CNF",            
    0x3802 :     "ID_CAS_CTTF_HRPD_SPS_COMMIT_NTF",                 
    0x3803 :     "ID_CAS_CTTF_HRPD_SPS_SEC_SHA1_CONFIG_REQ",        
    0x3804 :     "ID_CTTF_CAS_HRPD_SPS_ERROR_IND",                  
    0x3860 :     "ID_CTTF_CAS_HRPD_PA_RAT_MODE_IND",                
    0x3861 :     "ID_CAS_CTTF_HRPD_PA_COMMIT_REQ",                  
    0x3862 :     "ID_CTTF_CAS_HRPD_PA_RESERVATION_QOS_KK_IND",      
    0x3863 :     "ID_CAS_CTTF_HRPD_PA_RELEASE_ALL_REQ",             
    0x3864 :     "ID_CTTF_CAS_HRPD_PA_RELEASE_ALL_CNF",             
    0x3865 :     "ID_CAS_CTTF_HRPD_PA_CONNECTION_OPENED_REQ",       
    0x3866 :     "ID_CAS_CTTF_HRPD_PA_CONNECTION_CLOSED_REQ",       
    0x3867 :     "ID_CTTF_CAS_HRPD_PA_ERROR_IND",                   
    0x3868 :     "ID_CTTF_CAS_HRPD_PA_ACCESS_AUTH_DECISION_IND",    
    0x3869 :     "ID_CTTF_CAS_HRPD_PA_ACCESS_AUTH_STATUS_IND",      
    0x386A :     "ID_CTTF_CAS_HRPD_PA_OPEN_CONNECTION_IND",
    0x386B :     "ID_CTTF_CAS_HRPD_PA_TAP_TEST_ACTION_REQ",
    0x386C :     "ID_CAS_CTTF_HRPD_PA_TAP_TEST_ACTION_CNF",	
    0x33A0 :     "ID_CTTF_CNAS_HRPD_ACMAC_TXENDED_IND",             
    0x33A1 :     "ID_CTTF_CAS_HRPD_ACMAC_TXSTARTED_IND",            
    0x33A2 :     "ID_CTTF_CAS_HRPD_ACMAC_TXENDED_IND",              
    0x33A3 :     "ID_CTTF_CAS_HRPD_ACMAC_TRANSMISSION_SUCC_IND",    
    0x33A4 :     "ID_CTTF_CAS_HRPD_ACMAC_TRANSMISSION_FAIL_IND",    
    0x33A5 :     "ID_CTTF_CAS_HRPD_ACMAC_SUPERVISION_FAILED_IND",   
    0x33A6 :     "ID_CTTF_CAS_HRPD_RTCMAC_LINK_ACQUIRED_IND",       
    0x33A7 :     "ID_CTTF_CAS_HRPD_RTCMAC_SUPERVISON_FAILED_IND",   
    0x0001 :     "ID_PS_RRM_RADIO_RESOURCE_APPLY_REQ",              
    0x0003 :     "ID_PS_RRM_RADIO_RESOURCE_RELEASE_IND",
    0x0004 :     "ID_RFUSER_CAS_HRPD_RESOURCE_REL_NTF",	
    0x0005 :     "ID_PS_RRM_RADIO_RESOURCE_OCCUPY_CNF",             
    0x0006 :     "ID_PS_RRM_PROTECT_PS_IND",                        
    0x0007 :     "ID_PS_RRM_DEPROTECT_PS_IND",                      
    0x000D :     "ID_PS_RRM_PROTECT_SIGNAL_IND",                    
    0x000E :     "ID_PS_RRM_DEPROTECT_SIGNAL_IND",
}

def CTTF_GetMsgIdStr(usMsgId):
    if usMsgId in cproc_cttf_hrpd_msg_enum_table:
        strMsgId = '%s(0x%X)' % (cproc_cttf_hrpd_msg_enum_table[usMsgId], usMsgId)
    elif usMsgId in cas_cttf_hrpd_msg_enum_tabel:
        strMsgId = '%s(0x%X)' % (cas_cttf_hrpd_msg_enum_tabel[usMsgId], usMsgId)
    else:
        strMsgId = 'None(0x%X)' % (usMsgId)
    return strMsgId