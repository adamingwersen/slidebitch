import { Dispatch, SetStateAction, useEffect, useState } from "react";

export enum STORAGE_KEYS {
  QUERY_RESULT = "query_results",
  QUERY_STRING = "query_string",
}

// https://upmostly.com/next-js/using-localstorage-in-next-js
type SetValue<T> = Dispatch<SetStateAction<T>>;

export const useLocalStorage = <T,>(
  key: STORAGE_KEYS,
  fallbackValue?: T | null
): [T | undefined, SetValue<T>, () => void] => {
  let item;
  if (typeof window !== "undefined") {
    const storageItem = localStorage.getItem(key);
    item = JSON.parse(!!storageItem ? storageItem : "null");
  }

  const [value, setValue] = useState<T>(item ?? fallbackValue);

  const clearValue = () => {
    localStorage.removeItem(key);
  };

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue, clearValue];
};
