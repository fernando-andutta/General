%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Script to load excel file (3 sheets)
%
% INPUT INFORMATION: excell files (familyname_name_yyyy.xlsx)
% OUTPUT INFORMATION: report file and transferrence of good files to folder
% (PASSED) and bad files to folder (FAILED)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Additional information about process carried out
% 1 - script to check (1st level) information from Excel- input
% 2 - generates three main folders: BACKUP, FAILED and PASSED
% 3 - all files are saved into BACKUP for safety
% 4 - a report file is generated to both FAILED and PASSED files
% 5 - files with problems are sent to FAILED
% 6 - files that passed are sent to PASSED
% 7 - passed files (in PASSED) are automatically further removed from
% the folder (FAILED)
% 8 - files in folder PASSED are not processed again.
% author: Fernando Pinheiro Andutta
% data of update: 08/11/2019
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% preparing workspace
clear all
close all
clc
tic
time1 = toc;

%% saving path of current directory
path_maindir = pwd;

%% making folder names to transfer files according to categories
filename_backup = 'FOLDER_BACKUP';
filename_passed = 'FOLDER_PASSED_LEVEL1';
filename_failed = 'FOLDER_FAILED';

%% making folders to transfer files according to categories
mkdir(filename_backup);
mkdir(filename_passed);
mkdir(filename_failed);

%% path to saved files
path_backup = [path_maindir '\' filename_backup];
path_passed = [path_maindir '\' filename_passed];
path_failed = [path_maindir '\' filename_failed];

%% listing names in this directory
%files_this_level = dir(pwd); listing all contents
files_this_level = dir('*.xlsx');
files_this_level_size = size(files_this_level);
files_this_level_size = files_this_level_size(1,1);

%% loop to create all names
for xx=1:files_this_level_size;
files_this_level_aux = files_this_level(xx).name;
files_here{xx,1} = files_this_level_aux;
end % for xx=1;
clear files_this_*

kk_done=0; % used to exclude files already done
total_files_done = 0;
kk_notdone=0; % used to exclude files already done
total_files_notdone = 0;

total_files_passed = 0;
total_files_failed = 0;

%% loading files
for zz=1:length(files_here(:,1));   
%zz=1;
filename0 = char(files_here(zz,1));

% checking if file has already been done, and correctly
cd(path_passed);
filename0_passed = exist(filename0, 'file'); % 2 means exist
cd(path_maindir);

% checking if file has failed,
cd(path_failed);
filename0_failed = exist(filename0, 'file'); % 2 means exist
cd(path_maindir);

if filename0_passed==2; % processing only new files
% do nothing since it has been done
kk_done=kk_done+1;
total_files_done(kk_done)=1;

    if filename0_failed==2; % processing only new files
    cd(path_failed);
    filename0_report = [filename0, '_report.txt'];
    delete(filename0); % it has passed, so it can be deleted
    delete(filename0_report); % it has passed, so it can be deleted
    cd(path_maindir);
    end

else
kk_notdone=kk_notdone+1;
total_files_notdone(kk_notdone)=1;
    
    
MAIN_person_info_header = readtable(filename0,'Sheet','MAIN','Range','B9:H10');
MAIN_person_info_data = readtable(filename0,'Sheet','MAIN','Range','B11:H12');

MAIN_person_article_header = readtable(filename0,'Sheet','MAIN','Range','B15:H16');
MAIN_person_article_data = readtable(filename0,'Sheet','MAIN','Range','B17:H18');

CITATIONS_header = readtable(filename0,'Sheet','CITATIONS','Range','A3:J4');
CITATIONS_data = readtable(filename0,'Sheet','CITATIONS','Range','A10:J1010');

REFERENCES_header = readtable(filename0,'Sheet','REFERENCES','Range','A1:I2');
REFERENCES_data = readtable(filename0,'Sheet','REFERENCES','Range','A4:I1004');

%% converting tables to cell of arrays
MAIN_person_info_header = table2cell(MAIN_person_info_header);
MAIN_person_info_data = table2cell(MAIN_person_info_data);
MAIN_person_article_header = table2cell(MAIN_person_article_header);
MAIN_person_article_data = table2cell(MAIN_person_article_data);
CITATIONS_header = table2cell(CITATIONS_header);
CITATIONS_data = table2cell(CITATIONS_data);
REFERENCES_header = table2cell(REFERENCES_header);
REFERENCES_data = table2cell(REFERENCES_data);

%% reducing the table of CITATIONS
CITATIONS_indexes_notvalid = 0;
CITATIONS_indexes_valid = 0;

for xx=1:length(CITATIONS_data);

aux1 = CITATIONS_data(xx,2);
aux1_isempty = isempty(aux1{1,1}); % 1 for empty cell
if aux1_isempty==1
aux1_isnan = 0; % cannot be NAN
else
aux1_isnan = isnan(aux1{1,1}); % 1 for NAN cell
end
aux1_total = aux1_isempty + aux1_isnan;

if aux1_total>=1;
CITATIONS_indexes_notvalid = [CITATIONS_indexes_notvalid; xx];
else
CITATIONS_indexes_valid = [CITATIONS_indexes_valid; xx];
end

end
clear xx aux1*

CITATIONS_indexes_notvalid = CITATIONS_indexes_notvalid(2:end);
CITATIONS_indexes_valid = CITATIONS_indexes_valid(2:end);

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% QUALITY CHECKING SECTIONS - START %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% checking1 (for CITATIONS empty rows)
% check if CITATIONS are sequential (NO EMPTY ROWS ALOWED BETWEEN COMPLETED ROWS)
CITATIONS_indexes_valid_check = diff(CITATIONS_indexes_valid)==1;
CITATIONS_indexes_valid_check = nansum(double(CITATIONS_indexes_valid_check))+1;
% value must be equal to its array lenght
if CITATIONS_indexes_valid_check == length(CITATIONS_indexes_valid);
checking1 = 0;
else
checking1 = 1;
end

%% Reducing the table of REFERENCES
REFERENCES_indexes_notvalid = 0;
REFERENCES_indexes_valid = 0;

for xx=1:length(REFERENCES_data);

aux1 = REFERENCES_data(xx,2);
aux1_isempty = isempty(aux1{1,1}); % 1 for empty cell
if aux1_isempty==1
aux1_isnan = 0; % cannot be NAN
else
aux1_isnan = isnan(aux1{1,1}); % 1 for NAN cell
end
aux1_total = aux1_isempty + aux1_isnan;

if aux1_total>=1;
REFERENCES_indexes_notvalid = [REFERENCES_indexes_notvalid; xx];
else
REFERENCES_indexes_valid = [REFERENCES_indexes_valid; xx];
end

end
clear xx aux1*

REFERENCES_indexes_notvalid = REFERENCES_indexes_notvalid(2:end);
REFERENCES_indexes_valid = REFERENCES_indexes_valid(2:end);

%% checking2 (for REFERENCES empty rows)
% check if REFERENCES are sequential (NO EMPTY ROWS ALLOWED BETWEEN COMPLETED ROWS)
REFERENCES_indexes_valid_check = diff(REFERENCES_indexes_valid)==1;
REFERENCES_indexes_valid_check = nansum(double(REFERENCES_indexes_valid_check))+1;
% value must be equal to its array lenght
if REFERENCES_indexes_valid_check == length(REFERENCES_indexes_valid);
checking2 = 0;
else
checking2 = 1;
end

%% checking citations for critical required information
CITATIONS_data2 = CITATIONS_data(CITATIONS_indexes_valid,:);
clear CITATIONS_data;
REF_number_saved = 0;
CITATIONS_data2_row_classification_failed_all = 0;
CITATIONS_data2_row_position_failed_all = 0;
CITATIONS_data2_row_counter_R_failed_all = 0;
CITATIONS_data2_row_counter_R_failed_all = [0,0];

for xx=1:length(CITATIONS_data2(:,1));

CITATIONS_data2_row = CITATIONS_data2(xx,:);

CITATIONS_data2_row_piece = char(CITATIONS_data2_row(1,2));

% quality control - citation classification has been indicated
aux3 = CITATIONS_data2_row(1,3);
aux4 = CITATIONS_data2_row(1,4);
aux5 = CITATIONS_data2_row(1,5);
CITATIONS_data2_row_classification = strcat(aux3,aux4,aux5);
CITATIONS_data2_row_classification = strrep(CITATIONS_data2_row_classification,'x','X');
pos1 = strfind(char(CITATIONS_data2_row_classification),'X');
pos1 = length(pos1);


        if pos1==0 | pos1==3;
        CITATIONS_data2_row_classification_failed_all(xx,1) = 1;
        else
        CITATIONS_data2_row_classification_failed_all(xx,1) = 0;  
        end
        clear aux* pos1


% quality control - citation position has been indicated
aux6 = CITATIONS_data2_row(1,6);
aux7 = CITATIONS_data2_row(1,7);
aux8 = CITATIONS_data2_row(1,8);
aux9 = CITATIONS_data2_row(1,9);
aux10 = CITATIONS_data2_row(1,10);
CITATIONS_data2_row_position = strcat(aux6,aux7,aux8,aux9,aux10);
CITATIONS_data2_row_position = strrep(CITATIONS_data2_row_position,'x','X');
pos1 = strfind(char(CITATIONS_data2_row_position),'X');
pos1 = length(pos1);


        if pos1==0 | pos1>2;
        CITATIONS_data2_row_position_failed_all(xx,1) = 1;
        else
        CITATIONS_data2_row_position_failed_all(xx,1) = 0;        
        end    
        clear aux* pos1


% quality control counting #R and #%
CITATIONS_data2_row_piece = strrep(CITATIONS_data2_row_piece,'#r','#R');
pos1a = strfind(char(CITATIONS_data2_row_piece),'#R');
pos1b = strfind(char(CITATIONS_data2_row_piece),'#%');
pos1a_total = length(pos1a);
pos1b_total = length(pos1b);

pos1c = strfind(char(CITATIONS_data2_row_piece),'# %');
pos1d = strfind(char(CITATIONS_data2_row_piece),'##%');
pos1e = strfind(char(CITATIONS_data2_row_piece),'# #');

        if length(pos1a)>=1 & pos1b_total==1*pos1a_total & length(pos1c)==0 & length(pos1d)==0 & length(pos1e)==0;
        CITATIONS_data2_row_counter_R_failed_all(xx,1) = 0;
        else
        CITATIONS_data2_row_counter_R_failed_all(xx,1) = 1;   
        end
        
        if length(pos1c)==1 | length(pos1d)==1 | length(pos1e)==1;
        CITATIONS_data2_row_counter_R_failed_all(xx,2) = 1;   
        else
        CITATIONS_data2_row_counter_R_failed_all(xx,2) = 0;      
        end

% saving numbers from references in citations
        %if length(pos1a)>0 & pos1b_total==1*pos1a_total & length(pos1c)==0 & length(pos1d)==0 & length(pos1e)==0;
        if length(pos1a)>0 & pos1b_total==1*pos1a_total;
            for yy=1:length(pos1a);
            aa = pos1a(yy);
            bb = pos1b(yy);
            REF_number_saved_aux = str2num(CITATIONS_data2_row_piece(aa+2:bb-1));
            REF_number_saved = [REF_number_saved; REF_number_saved_aux];
            end
        end
        clear yy


end
clear xx pos* aa bb

%% checking3 (have all citations been classified)
CITATIONS_data2_row_classification_failed = nansum(CITATIONS_data2_row_classification_failed_all);
% to inform about missing classification

min_citation_accepted = 6;

        if CITATIONS_data2_row_classification_failed>0 | length(CITATIONS_data2_row_classification_failed_all)<=min_citation_accepted;
        checking3=1;
        else
        checking3=0;
        end
        
        if length(CITATIONS_data2_row_classification_failed_all)<=min_citation_accepted; 
        checking3b=1;
        else
        checking3b=0;
        end;
     

%% checking4 (have all positions of citations been indicated)
CITATIONS_data2_row_position_failed = nansum(CITATIONS_data2_row_position_failed_all);
% to inform about missing position indication

min_citation_accepted = min_citation_accepted;

        if CITATIONS_data2_row_position_failed>0 | length(CITATIONS_data2_row_position_failed_all)<=min_citation_accepted;
        checking4=1;
        else
        checking4=0;
        end
        
        if length(CITATIONS_data2_row_position_failed_all)<=min_citation_accepted; 
        checking4b=1;
        else
        checking4b=0;
        end;
        
        
%% checking5 (have all indexes #R and # been properly applied
CITATIONS_data2_row_counter_R_failed = nansum(CITATIONS_data2_row_counter_R_failed_all(:,1))+nansum(CITATIONS_data2_row_counter_R_failed_all(:,2));
% to inform about missing #R and # around the numbers within every citation

min_citation_accepted = min_citation_accepted;

        if CITATIONS_data2_row_counter_R_failed>0 | length(CITATIONS_data2_row_counter_R_failed_all)<=min_citation_accepted;
        checking5=1;
        else
        checking5=0;
        end

        if length(CITATIONS_data2_row_position_failed_all)<=min_citation_accepted; 
        checking5b=1;
        else
        checking5b=0;
        end;
        
        clear min_citation_accepted;
                
%% checking6 (have all references (from sheet-REFERENCES) been cited (in sheet-CITATIONS)

if length(REF_number_saved)<=1;
checking6=1;
checking6b=1;
else
REF_number_saved = REF_number_saved(2:end);
REF_number_saved = sort(REF_number_saved);
REF_number_saved = unique(REF_number_saved);
REF_number_aux = REF_number_saved(1):1:REF_number_saved(end);
REF_number_aux = REF_number_aux';
REF_number_missing2cite=setdiff(REF_number_aux,REF_number_saved);
REF_number_missing2cite_all = REF_number_missing2cite;

% to inform about reference (sheet-REFERENCES) which were not cited in
% (sheet-CITATIONS)
if length(REF_number_missing2cite)>0;
checking6=1;
else
checking6=0;
end

checking6b=0;
end % if length(REF_number_saved)==0;
clear REF_number_saved REF_number_aux

%% checking7 (have all columns in REFERENCES been filled)
% references for critical required information
REFERENCES_data2_failed_all = 0;

if length(REFERENCES_indexes_valid)==0;

else % if length(REFERENCES_indexes_valid)==0;
    
REFERENCES_data2 = REFERENCES_data(REFERENCES_indexes_valid,:);

for mm=1:length(REFERENCES_data2(:,1));

REFERENCES_data2_aux = REFERENCES_data2(mm,:);

% aux2 = char(REFERENCES_data2_aux(1,2));
% aux3 = char(REFERENCES_data2_aux(1,3));
% aux4 = char(REFERENCES_data2_aux(1,4));
% aux5 = num2str(REFERENCES_data2_aux{1,5});
% aux6 = char(REFERENCES_data2_aux(1,6));
% aux7 = char(REFERENCES_data2_aux(1,7));
% aux8 = char(REFERENCES_data2_aux(1,8));
% aux9 = char(REFERENCES_data2_aux(1,9));

aux2 = char(cell2mat(REFERENCES_data2_aux(1,2)));
aux3 = char(cell2mat(REFERENCES_data2_aux(1,3)));
aux4 = char(cell2mat(REFERENCES_data2_aux(1,4)));
aux5 = num2str(REFERENCES_data2_aux{1,5});
aux6 = char(cell2mat(REFERENCES_data2_aux(1,6)));
aux7 = char(cell2mat(REFERENCES_data2_aux(1,7)));
aux8 = char(cell2mat(REFERENCES_data2_aux(1,8)));
aux9 = char(cell2mat(REFERENCES_data2_aux(1,9)));


        if length(aux2)<6 | length(aux3)<3 | length(aux4)<3 | length(aux5)<4 | length(aux6)<1 | length(aux7)<1 | length(aux8)<1 | length(aux9)<1;
        REFERENCES_data2_failed_all(mm,1)=1;
        else
        REFERENCES_data2_failed_all(mm,1)=0;
        end
    
end % for
clear xx aux*

checking7b = 0;
end % if length(REFERENCES_indexes_valid)==0;

REFERENCES_data2_failed = nansum(REFERENCES_data2_failed_all);
checking7 = REFERENCES_data2_failed;

if length(REFERENCES_indexes_valid)==0;
checking7 = 1;
checking7b = 1; %no indexes for references
end

%% if sheets CITATIONS and REFERENCES are mostly empty, reject file
checking_3b_to_7b = checking3b+checking4b+checking5b+checking6b+checking7b;
if checking_3b_to_7b>=1;
warning('File mostly empty for sheet CITATIONS and REFERENCES');
pause(1);
warning('Aborting process for this file');
pause(1);
else
end % if checking_3b_to_7b>=1;

%% checking8 PERSON INFORMATION (have all cells of personal information been completed)

if checking_3b_to_7b>=1;
checking8 = 1;
MAIN_person_info_data_failed_familyname=1;
MAIN_person_info_data_failed_email=1;
else % if checking_3b_to_7b>=1;
    
aux1 = char(MAIN_person_info_data(1,1));
aux2 = char(MAIN_person_info_data(1,2));
aux3 = char(MAIN_person_info_data(1,3));
aux4 = char(MAIN_person_info_data(1,4));
aux5 = char(MAIN_person_info_data(1,5));
aux6 = char(MAIN_person_info_data(1,6));
aux7 = char(MAIN_person_info_data(1,7));

        if length(aux1)<1 | length(aux2)<1 | length(aux3)<1 | length(aux4)<1 | length(aux5)<1 | length(aux6)<1 | length(aux7)<1;
        MAIN_person_info_data_failed = 1;
        else
        MAIN_person_info_data_failed = 0;
        end

% converting all letters to small
aux1_small = lower(aux1);
aux2_small = lower(aux2);
aux3_small = lower(aux3);


% aux1_small; FAMILY NAME small letters
pos1 = strfind(aux1_small,' ');
if length(pos1)==0;
aux1_small_firstword = aux1_small;
else
aux1_small_firstword = aux1_small(1:pos1-1);   
end
% aux1_small_firstword ;1st word from family name small letters

% aux2_small; FIRST NAME;
% aux2_small_startletter; 1st letter of first name;
aux2_small_startletter = aux2_small(1);

% aux3_small_firstword; getting first word used for citation
pos1 = strfind(aux3_small,',');
if length(pos1)==0;
aux3_small_firstword = 'not found';   
else
pos1 = pos1(1);
aux3_small_firstword = aux3_small(1:pos1-1);    
end


% aux3_small = name for CITATION
pos1 = strfind(aux1_small,aux3_small_firstword);
if length(pos1)==0;
MAIN_person_info_data_failed_familyname=1;
else
MAIN_person_info_data_failed_familyname=0;
end

% checking if email contains @
pos1 = strfind(aux4,'@');
if length(pos1)==0;
MAIN_person_info_data_failed_email=1;
else
MAIN_person_info_data_failed_email=0;
end

MAIN_person_info_data_failed = MAIN_person_info_data_failed+MAIN_person_info_data_failed_familyname+...
    MAIN_person_info_data_failed_email;

        clear aux*
checking8 = MAIN_person_info_data_failed;

end % if checking_3b_to_7b>=1;
    
%% checking9 ARTICLE INFORMATION (have all cells of article information been completed)

if checking_3b_to_7b>=1;
checking9 = 1;
MAIN_person_article_data_failed_yn = 1;
MAIN_person_article_data_failed_year = 1;
else % if checking_3b_to_7b>=1;
    
aux1 = cell2mat(MAIN_person_article_data(1,1));
aux2 = cell2mat(MAIN_person_article_data(1,2));
aux3 = cell2mat(MAIN_person_article_data(1,3));
aux4 = cell2mat(MAIN_person_article_data(1,4));
aux5 = cell2mat(MAIN_person_article_data(1,5));
aux6 = cell2mat(MAIN_person_article_data(1,6));
aux7 = cell2mat(MAIN_person_article_data(1,7));

        if length(aux1)<1 | length(aux2)<1 | length(aux3)<1 | length(aux4)<1 | length(aux5)<1 | length(aux6)<1 | length(aux7)<1;
        MAIN_person_article_data_failed = 1;
        else
        MAIN_person_article_data_failed = 0;
        end

aux1 = lower(aux1);
pos1a = strfind(aux1,'y');    
pos1b = strfind(aux1,'n'); 
pos1 = length(pos1a)+length(pos1b);

if pos1==1;
MAIN_person_article_data_failed_yn = 0;
else
MAIN_person_article_data_failed_yn = 1;
end
if length(aux5)==4;
MAIN_person_article_data_failed_year = 0;
else
MAIN_person_article_data_failed_year = 1;
end

        clear aux*
checking9 = MAIN_person_article_data_failed;

end % if checking_3b_to_7b>=1;

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% QUALITY CHECKING SECTIONS - END %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Copy files into backup folder
copyfile(filename0,path_backup);

%% FINAL STATUS
failed_all(zz) = checking1+checking2+checking3+checking4+checking5+checking6+checking7+checking8+checking9;
failed_all_aux = failed_all(zz);

%% Copy files that have passed quality check
if failed_all_aux==0;
copyfile(filename0,path_passed);
else
copyfile(filename0,path_failed);
end

%% writing the status report
if failed_all_aux==0;
total_files_passed = total_files_passed + 1;
cd(path_passed);
else
cd(path_failed);
total_files_failed = total_files_failed + 1;
end

%% saving the report file
filename0_red = strrep(filename0,'.xlsx','');
fid=fopen([filename0 '_report.txt'],'w');

% HEADER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%';
fprintf(fid,'%6.200s\n',msg_aux');
fprintf(fid,'%6.200s\n',msg_aux');
msg_aux = '%%% Below you see questions regarding what is needed to be corrected %%%';
fprintf(fid,'%6.200s\n',msg_aux'); 
msg_aux = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%';
fprintf(fid,'%6.200s\n',msg_aux');
fprintf(fid,'%6.200s\n',msg_aux');

% checking1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '1 - Does the Excel(sheet-CITATIONS) passed test (empty-rows)? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking1>=1;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please check for empty rows in the Excel(sheet-CITATIONS), since completed rows cannot have empty rows between them';
else
msg_aux = 'PASSED. Thank you!';   
end % if checking1==1;
fprintf(fid,'%6.200s\n',msg_aux'); 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% checking2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '2 - Does the Excel(sheet-REFERENCES) passed test (empty-rows)? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking2>=1;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please remove check for empty rows in the Excel(sheet-REFERENCES), since completed rows cannot have empty rows between them';
else
msg_aux = 'PASSED. Thank you!';   
end %if checking2==1;
fprintf(fid,'%6.200s\n',msg_aux'); 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% checking3 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '3 - Have all citations been classified, and properly? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking3>=1 & checking3b==0;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please check for issues about classification of citations in rows:';
fprintf(fid,'%6.200s\n',msg_aux'); 
    for yy=1:length(CITATIONS_data2_row_classification_failed_all);
        if CITATIONS_data2_row_classification_failed_all(yy)==1;
        aux = CITATIONS_data2{yy,1};
        msg_aux = [aux];
        fprintf(fid,'%6.200s\n',msg_aux');
        end
    end
else

if checking3b==1;
fprintf(fid,'\n');
msg_aux = 'FAILED. No data found!';  
fprintf(fid,'%6.200s\n',msg_aux');  
else
msg_aux = 'PASSED. Thank you!';  
fprintf(fid,'%6.200s\n',msg_aux');
end % if checkingNb>=1;

end %if checking3==1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% checking4 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '4 - Have all positions of citations been defined, and properly? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking4>=1 & checking4b==0;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please check for issues regarding position for citations in rows:';
fprintf(fid,'%6.200s\n',msg_aux'); 
    for yy=1:length(CITATIONS_data2_row_position_failed_all);
        if CITATIONS_data2_row_position_failed_all(yy)==1;
        aux = CITATIONS_data2{yy,1};
        msg_aux = [aux];
        fprintf(fid,'%6.200s\n',msg_aux');
        end
    end
else
    
if checking4b==1;
fprintf(fid,'\n');
msg_aux = 'FAILED. No data found!';  
fprintf(fid,'%6.200s\n',msg_aux');  
else
msg_aux = 'PASSED. Thank you!';  
fprintf(fid,'%6.200s\n',msg_aux');
end % if checkingNb>=1;

end %if checking4==1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% checking5 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '5 - Have all indexes-holder (#R) and (#%) been properly applied to the numbers (e.g. #Rnumber#%) of references in the citations-columns in (sheet-CITATIONS)? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking5>=1 & checking5b==0;
fprintf(fid,'\n'); 
msg_aux = 'FAILED. Please check for issues regarding (#R or #%):';
fprintf(fid,'%6.200s\n',msg_aux'); 
%
    for yy=1:length(CITATIONS_data2_row_counter_R_failed_all);
        if CITATIONS_data2_row_counter_R_failed_all(yy,1)==1;
        aux = CITATIONS_data2{yy,1};
        msg_aux = [aux];
        fprintf(fid,'%6.200s\n',msg_aux');
        end
    end
    
    msg_aux = 'FAILED. Please check for issues regarding (# #% or # % or # #):';
fprintf(fid,'%6.200s\n',msg_aux'); 
%
    for yy=1:length(CITATIONS_data2_row_counter_R_failed_all);
        if CITATIONS_data2_row_counter_R_failed_all(yy,2)==1;
        aux = CITATIONS_data2{yy,1};
        msg_aux = [aux];
        fprintf(fid,'%6.200s\n',msg_aux');
        end
    end
%
%
else

if checking5b==1;
fprintf(fid,'\n');
msg_aux = 'FAILED. No data found!';  
fprintf(fid,'%6.200s\n',msg_aux');  
else
msg_aux = 'PASSED. Thank you!';  
fprintf(fid,'%6.200s\n',msg_aux');
end % if checkingNb>=1;

end % if checking5==1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% checking6 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '6 - Have all references been cited in sheet-CITATIONS? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking6>=1 & checking6b==0;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please check for references missing to be cited:';
fprintf(fid,'%6.200s\n',msg_aux'); 
    for yy=1:length(REF_number_missing2cite_all);
        aux = REF_number_missing2cite_all(yy);
        msg_aux = ['#R' num2str(aux) '#%'];
        fprintf(fid,'%6.200s\n',msg_aux');
    end
else
    
if checking6b==1;
fprintf(fid,'\n');
msg_aux = 'FAILED. No data found!';  
fprintf(fid,'%6.200s\n',msg_aux');  
else
msg_aux = 'PASSED. Thank you!';  
fprintf(fid,'%6.200s\n',msg_aux');
end % if checkingNb>=1;

end %if checking6==1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% checking7 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '7 - Have you completed all cells in sheet-REFERENCES? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking7>=1 & checking7b==0;;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please check all years and consider using (N/A) for empty cells, so that we know it was not left by accident:';
fprintf(fid,'%6.200s\n',msg_aux'); 
    for yy=1:length(REFERENCES_data2_failed_all);
        aux = REFERENCES_data2_failed_all(yy);
        if aux==1;
        msg_aux = char(REFERENCES_data2(yy));
        fprintf(fid,'%6.200s\n',msg_aux');
        end
    end
else
    
if checking7b==1;
fprintf(fid,'\n');
msg_aux = 'FAILED. No data found!';  
fprintf(fid,'%6.200s\n',msg_aux');  
else
msg_aux = 'PASSED. Thank you!';  
fprintf(fid,'%6.200s\n',msg_aux');
end % if checkingNb>=1;

end %if checking7==1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% checking8 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '8 - Have you completed your personal information for cells in sheet-MAIN? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking8>=1 & checking_3b_to_7b==0;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please consider using (N/A) for empty cells, so that we know it was not left by accident.';
fprintf(fid,'%6.200s\n',msg_aux'); 
else

if checking_3b_to_7b>=1;
fprintf(fid,'\n');
msg_aux = 'FAILED. This check-step was aborted due to main issues in CITATIONS and REFERENCES!';  
fprintf(fid,'%6.200s\n',msg_aux'); 
else
msg_aux = 'PASSED. Thank you!';  
fprintf(fid,'%6.200s\n',msg_aux'); 
end

end %if checking8==1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if checking8>=1;
if MAIN_person_info_data_failed_familyname==1;
msg_aux = 'Check your family name in sheet-MAIN cell(D12)';
fprintf(fid,'%6.200s\n',msg_aux'); 
end

if MAIN_person_info_data_failed_email==1;
msg_aux = 'Check your email in sheet-MAIN cell(E12)';
fprintf(fid,'%6.200s\n',msg_aux'); 
end
end


% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




% checking9 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
msg_aux = '9 - Have you completed the information of your published article for cells in sheet-MAIN? ';
fprintf(fid,'%6.200s',msg_aux'); 
if checking9>=1 & checking_3b_to_7b==0;
fprintf(fid,'\n');
msg_aux = 'FAILED. Please consider using (N/A) for empty cells, so that we know it was not left by accident.';
fprintf(fid,'%6.200s\n',msg_aux'); 
else

if checking_3b_to_7b>=1;
fprintf(fid,'\n');
msg_aux = 'FAILED. This check-step was aborted due to main issues in CITATIONS and REFERENCES!';  
fprintf(fid,'%6.200s\n',msg_aux'); 
else
msg_aux = 'PASSED. Thank you!';  
fprintf(fid,'%6.200s\n',msg_aux'); 
end
    
end %if checking9==1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


if checking9>=1 & checking_3b_to_7b==0;
if MAIN_person_article_data_failed_yn==1;
msg_aux = 'Please check the year number which should be in the format YYYY (For example: 2018).';
fprintf(fid,'%6.200s\n',msg_aux'); 
end
if MAIN_person_article_data_failed_year==1 & checking_3b_to_7b==0;
%msg_aux = 'MMMMMMMMMMMMMMMMMMMMMMMM';
%fprintf(fid,'%6.200s\n',msg_aux'); 
end
end



msg_aux = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%';
fprintf(fid,'%6.200s\n',msg_aux');
fprintf(fid,'%6.200s\n',msg_aux');
msg_aux = '%%%% Thank you for providing quality assurance on your contribution %%%%';
fprintf(fid,'%6.200s\n',msg_aux'); 
msg_aux = '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%';
fprintf(fid,'%6.200s\n',msg_aux');
fprintf(fid,'%6.200s\n',msg_aux');

fclose(fid);
cd(path_maindir);

end % if filename0_passed==2;

end % for zz=1:length(files_here(xx,1));

processing_time_seconds = toc - time1
total_files_done = nansum(total_files_done);
total_files_notdone = nansum(total_files_notdone);

files_processed_before = total_files_done
files_new_and_just_processed = total_files_notdone

if total_files_notdone==0;
else
average_processing_time_per_file = processing_time_seconds/total_files_notdone
total_files_passed = total_files_passed
total_files_failed = total_files_failed
end
clear processing_time_seconds time1 total_files average_processing_time_per_file
clear files_processed_before files_new_and_just_processed





