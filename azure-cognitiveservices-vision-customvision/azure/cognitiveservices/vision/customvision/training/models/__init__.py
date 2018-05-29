# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .domain_py3 import Domain
    from .image_tag_py3 import ImageTag
    from .image_region_py3 import ImageRegion
    from .image_py3 import Image
    from .image_create_result_py3 import ImageCreateResult
    from .image_create_summary_py3 import ImageCreateSummary
    from .region_py3 import Region
    from .image_file_create_entry_py3 import ImageFileCreateEntry
    from .image_file_create_batch_py3 import ImageFileCreateBatch
    from .image_url_create_entry_py3 import ImageUrlCreateEntry
    from .image_url_create_batch_py3 import ImageUrlCreateBatch
    from .image_id_create_entry_py3 import ImageIdCreateEntry
    from .image_id_create_batch_py3 import ImageIdCreateBatch
    from .image_tag_create_entry_py3 import ImageTagCreateEntry
    from .image_tag_create_batch_py3 import ImageTagCreateBatch
    from .image_tag_create_summary_py3 import ImageTagCreateSummary
    from .image_region_create_entry_py3 import ImageRegionCreateEntry
    from .image_region_create_batch_py3 import ImageRegionCreateBatch
    from .image_region_create_result_py3 import ImageRegionCreateResult
    from .image_region_create_summary_py3 import ImageRegionCreateSummary
    from .bounding_box_py3 import BoundingBox
    from .region_proposal_py3 import RegionProposal
    from .image_region_proposal_py3 import ImageRegionProposal
    from .prediction_query_tag_py3 import PredictionQueryTag
    from .prediction_query_token_py3 import PredictionQueryToken
    from .prediction_py3 import Prediction
    from .stored_image_prediction_py3 import StoredImagePrediction
    from .prediction_query_result_py3 import PredictionQueryResult
    from .image_url_py3 import ImageUrl
    from .image_prediction_py3 import ImagePrediction
    from .iteration_py3 import Iteration
    from .project_settings_py3 import ProjectSettings
    from .project_py3 import Project
    from .tag_performance_py3 import TagPerformance
    from .iteration_performance_py3 import IterationPerformance
    from .image_performance_py3 import ImagePerformance
    from .export_py3 import Export
    from .tag_py3 import Tag
except (SyntaxError, ImportError):
    from .domain import Domain
    from .image_tag import ImageTag
    from .image_region import ImageRegion
    from .image import Image
    from .image_create_result import ImageCreateResult
    from .image_create_summary import ImageCreateSummary
    from .region import Region
    from .image_file_create_entry import ImageFileCreateEntry
    from .image_file_create_batch import ImageFileCreateBatch
    from .image_url_create_entry import ImageUrlCreateEntry
    from .image_url_create_batch import ImageUrlCreateBatch
    from .image_id_create_entry import ImageIdCreateEntry
    from .image_id_create_batch import ImageIdCreateBatch
    from .image_tag_create_entry import ImageTagCreateEntry
    from .image_tag_create_batch import ImageTagCreateBatch
    from .image_tag_create_summary import ImageTagCreateSummary
    from .image_region_create_entry import ImageRegionCreateEntry
    from .image_region_create_batch import ImageRegionCreateBatch
    from .image_region_create_result import ImageRegionCreateResult
    from .image_region_create_summary import ImageRegionCreateSummary
    from .bounding_box import BoundingBox
    from .region_proposal import RegionProposal
    from .image_region_proposal import ImageRegionProposal
    from .prediction_query_tag import PredictionQueryTag
    from .prediction_query_token import PredictionQueryToken
    from .prediction import Prediction
    from .stored_image_prediction import StoredImagePrediction
    from .prediction_query_result import PredictionQueryResult
    from .image_url import ImageUrl
    from .image_prediction import ImagePrediction
    from .iteration import Iteration
    from .project_settings import ProjectSettings
    from .project import Project
    from .tag_performance import TagPerformance
    from .iteration_performance import IterationPerformance
    from .image_performance import ImagePerformance
    from .export import Export
    from .tag import Tag
from .training_api_enums import (
    DomainType,
    ImageUploadStatus,
    OrderBy,
    ExportPlatform,
    ExportStatusModel,
    ExportFlavor,
)

__all__ = [
    'Domain',
    'ImageTag',
    'ImageRegion',
    'Image',
    'ImageCreateResult',
    'ImageCreateSummary',
    'Region',
    'ImageFileCreateEntry',
    'ImageFileCreateBatch',
    'ImageUrlCreateEntry',
    'ImageUrlCreateBatch',
    'ImageIdCreateEntry',
    'ImageIdCreateBatch',
    'ImageTagCreateEntry',
    'ImageTagCreateBatch',
    'ImageTagCreateSummary',
    'ImageRegionCreateEntry',
    'ImageRegionCreateBatch',
    'ImageRegionCreateResult',
    'ImageRegionCreateSummary',
    'BoundingBox',
    'RegionProposal',
    'ImageRegionProposal',
    'PredictionQueryTag',
    'PredictionQueryToken',
    'Prediction',
    'StoredImagePrediction',
    'PredictionQueryResult',
    'ImageUrl',
    'ImagePrediction',
    'Iteration',
    'ProjectSettings',
    'Project',
    'TagPerformance',
    'IterationPerformance',
    'ImagePerformance',
    'Export',
    'Tag',
    'DomainType',
    'ImageUploadStatus',
    'OrderBy',
    'ExportPlatform',
    'ExportStatusModel',
    'ExportFlavor',
]