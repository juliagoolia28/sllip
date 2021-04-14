function run_froi_resp_mag(opts)

%% Measure response magnitudes in frois

% opts.PROJECT_DIR = '/Volumes/data-1/users/julie/make_parcels-julie/';
% opts.PARCEL_DIR = [PROJECT_DIR 'parcels/ssl_str_rd_50pct_thresh2.326_14-Apr-2021/'];
% opts.PARCEL_FILE = [PARCEL_DIR 'ssl_str_rd_probability_map_thresh2subjs_smoothed_parcels_sig.nii.gz'];
% 
% opts.SUBJ_DEFINE_DATA_DIR = [PROJECT_DIR 'data/sllip/ssl_structured/'];
% opts.SUBJ_MEASURE_DATA_DIR = [PROJECT_DIR 'data/sllip/ssl_structured_copes/'];
% 
% opts.RESULTS_DIR = [PROJECT_DIR 'data/froi_analysis_results/'];
% if ~exist(opts.RESULTS_DIR,'dir')
%     mkdir(opts.RESULTS_DIR)
% end
% 
% % Conditions to measure
% opts.COND = {'sllip_ssl_str_v_rd_contrast'};
% opts.SUBJ_IDS = 1:30;

if isfloat(opts.SUBJ_IDS)
    for i = 1:length(opts.SUBJ_IDS)
        SUBJ_ID_STR{i} =['subj_' num2str(opts.SUBJ_IDS(i))];
    end
end

%% Load parcels

PARCEL_VOL = MRIread(opts.PARCEL_FILE,0);
vol_vals = unique(PARCEL_VOL.vol);
parcel_nums = vol_vals(vol_vals > 0);

for i = 1:length(parcel_nums)
    PARCEL_NUM_STR{i} =['parcel_' num2str(parcel_nums(i))];
end

%% For each parcel...

n_subjs = length(opts.SUBJ_IDS);
n_parcels = length(parcel_nums);

% For each subject
for i = 1:n_subjs

    % Load stat map for defining frois
    DEFINE_VOL = MRIread([opts.SUBJ_DEFINE_DATA_DIR num2str(opts.SUBJ_IDS(i)) '_zstat.nii.gz'],0);
    % Load cope(s) for measuring response
    MEASURE_VOL = MRIread([opts.SUBJ_MEASURE_DATA_DIR num2str(opts.SUBJ_IDS(i)) '_cope.nii.gz'],0);
    
    % For each parcel
    for j = 1:n_parcels
        
        temp_mask = PARCEL_VOL.vol == parcel_nums(j);
        mean_in_roi(i,j) = MeanCopeFROI(temp_mask,DEFINE_VOL.vol,MEASURE_VOL.vol);
        
    end

end

%% Setup results structure
results = array2table(mean_in_roi,'VariableNames',PARCEL_NUM_STR,'RowNames',SUBJ_ID_STR);
writetable(results,'/Volumes/data-1/users/julie/make_parcels-julie/froi_analysis_results/sllip_ssl_rd_vs_str_contrast_froi_resp_mag_60pct_2.326.csv')
end

function mean_in_roi = MeanCopeFROI(parcel_mask_vol,defining_vol,testing_vol)

% Mask defining volume with parcel
% Parcel mask should just be ones and zeros
voxel_idxs_in_parcel = find(parcel_mask_vol);

% Find top 10% of voxels
defining_data_voxel_values = defining_vol(voxel_idxs_in_parcel);
[~,sorted_voxel_idxs] = sort(defining_data_voxel_values,1,'descend');

n_voxels = length(voxel_idxs_in_parcel);
tenpct_n_voxels = round(n_voxels*0.10);

tenpct_sorted_voxel_idxs = sorted_voxel_idxs(1:tenpct_n_voxels);

testing_data_voxel_values = testing_vol(voxel_idxs_in_parcel);

tenpct_testing_data_values = testing_data_voxel_values(tenpct_sorted_voxel_idxs);

mean_in_roi = mean(tenpct_testing_data_values);
end