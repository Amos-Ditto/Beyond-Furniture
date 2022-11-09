import { defineStore } from "pinia";
import { Categories } from "~~/Types/common";

export const useSearchStore = defineStore("search", () => {
	const categories = ref<Categories[]>([
		{ Name: "all categories", id: 6 },
		{ Name: "Living Room", id: 1 },
		{ Name: "Bed Room", id: 2 },
		{ Name: "kitchen Dining", id: 3 },
		{ Name: "Office Furniture", id: 4 },
		{ Name: "others", id: 5 },
	]);
	const searchdata = ref<string>("");
	const selectedcategory = ref<Categories>({ Name: "", id: 0 });

	const updateSearchData = (payload: string): void => {
		searchdata.value = payload;
	};

	const updateSelectedCategory = (payload: Categories): void => {
		selectedcategory.value = payload;
	};

	const updateCategories = (payload: Categories[]) => {
		categories.value = payload;
	};

	return { categories, searchdata, selectedcategory, updateSearchData, updateSelectedCategory, updateCategories };
});
