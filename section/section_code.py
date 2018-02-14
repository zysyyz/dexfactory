# -- coding: utf-8 --

from section_base import *

class CodeSection(BaseSection):
	"""
	section: code_item
	"""

	def __init__(self, context, bytes, size, off):
		"""
		初始化
		context:   上下文信息
		bytes:     原始字节数组
		size:      子项总个数
		off:       字节数组偏移
		"""
		super(CodeSection, self).__init__(context, TYPE_CODE_ITEM, bytes[off:], size)

