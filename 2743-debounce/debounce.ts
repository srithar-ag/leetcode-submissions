// Type definition for a function that accepts any parameters and returns any value
type F = (...p: any[]) => any;

/**
 * Creates a debounced version of the provided function that delays its execution
 * until after the specified timeout has elapsed since the last time it was invoked.
 * 
 * @param fn - The function to debounce
 * @param t - The delay time in milliseconds
 * @returns A debounced version of the input function
 */
function debounce(fn: F, t: number): F {
    // Store the timeout ID to track and cancel pending executions
    let timeoutId: ReturnType<typeof setTimeout> | undefined;

    // Return a new function that wraps the original function with debouncing logic
    return function (this: any, ...args: any[]): void {
        // Clear any existing timeout to cancel the previous pending execution
        if (timeoutId !== undefined) {
            clearTimeout(timeoutId);
        }
      
        // Set a new timeout to execute the function after the specified delay
        timeoutId = setTimeout(() => {
            // Execute the original function with the correct context and arguments
            fn.apply(this, args);
        }, t);
    };
}

/**
 * Example usage:
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
