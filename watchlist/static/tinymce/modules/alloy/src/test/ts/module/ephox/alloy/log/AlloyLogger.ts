import { Element } from '@ephox/sugar';

// Used for atomic testing where window is not available.
const element = (elem: Element) => {
  return elem;
};

export {
  element
};
