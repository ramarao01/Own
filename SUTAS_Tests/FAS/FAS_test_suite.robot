*** Settings ***
Resource          variables.txt
Library           FASLib.FAS    WITH NAME    FAS

*** Variables ***

*** Test Cases ***
Aggregate_Creation
    FAS.Connect    ${ip}    ${username}    ${password}
    ${list_aggr}=    FAS.Aggr Show    &{args}
    FAS.Parser    ${list_aggr}
    FAS.Aggregate Create    &{aggr_createargs}
    FAS.Aggr Delete    &{aggr_deleteargs}
    FAS.Close

SVM_Creation
    FAS.Connect    ${ip}    ${username}    ${password}
    FAS.Network Interface Create    &{lif_createargs}
    FAS.Vserver Create    &{vserver_createargs}
    FAS.Network Interface Delete    &{lif_delargs}
    FAS.Volume Offline    &{rootvol_offlineargs}
    FAS.Volume Delete    &{rootvol_offlineargs}
    FAS.Vserver Delete    &{vserver_delargs}
    FAS.Volume Offline    &{rootvol_offlineargs}
    FAS.Close

Volume_Creation
    [Tags]    vc
    FAS.Connect    ${ip}    ${username}    ${password}
    FAS.Volume Create    &{vol_createargs}
    FAS.Lun Create    &{lun_createargs}
    ${list_lun}=    FAS.Lun Show    &{lun_vs_and_path_args}
    FAS.Close

resize_lun
    [Tags]    new
    FAS.Connect    ${ip}    ${username}    ${password}
    FAS.Lun Resize    &{lun_resize_args}
    FAS.Lun Show    &{lun_vs_and_path_args}
    FAS.Close

lun_modify
    FAS.Connect    ${ip}    ${username}    ${password}
    FAS.Lun Show    fields=space-reserve    &{lun_vs_and_path_args}
    FAS.Lun Modify    &{lun_modify_args}
    FAS.Lun Show    fields=space-reserve    &{lun_vs_and_path_args}
    FAS.Close

vol_and_lun_delete
    [Tags]    vl
    FAS.Connect    ${ip}    ${username}    ${password}
    Lun Delete    &{lun_vs_and_path_args}
    FAS.Volume Offline    &{vol_offlineargs}
    FAS.Volume Delete    &{vol_offlineargs}
    FAS.Lun Show    fields=space-reserve    &{lun_vs_and_path_args}
    FAS.Close
