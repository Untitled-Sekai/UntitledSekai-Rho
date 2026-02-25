import yaml
from enum import Enum
from pathlib import Path
from typing import Any, Optional

class Language(Enum):
    """
    追加したいときは、新しく追加してね。localizationディレクトリにもymlを新しくいれてね
    """
    JAPANESE = 'ja'
    ENGLISH = 'en'

class Localization:
    _cache: dict[str, dict[str, Any]] = {}
    _locale_dir = Path(__file__).parent / "localization"
    
    def __init__(self, lang: Language):
        self.language = lang
        self._load_language_file()
    
    def _load_language_file(self) -> None:
        """言語ファイルをキャッシュから読み込むか、ファイルから読み込む"""
        lang_code = self.language.value
        
        if lang_code not in Localization._cache:
            file_path = Localization._locale_dir / f"{lang_code}.yml"
            if not file_path.exists():
                raise FileNotFoundError(f"言語ファイルが見つかりません: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                Localization._cache[lang_code] = yaml.safe_load(f) or {}
        
        self.data = Localization._cache[lang_code]
    
    def get(self, key: str, default: Optional[str] = None) -> str:
        """
        ネストされたキーでテキストを取得する
        例: "sonolus.login" → data['sonolus']['login']
        """
        keys = key.split('.')
        value = self.data
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default if default is not None else f"[missing: {key}]"
            else:
                return default if default is not None else f"[invalid: {key}]"
        
        return str(value) if value is not None else (default or f"[missing: {key}]")